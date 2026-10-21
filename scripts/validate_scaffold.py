#!/usr/bin/env python3
"""Validate the public Elf-Books scaffold and private campaign snapshots.

Structural checks only. Passing does not mean game mechanics are approved.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_DOCS = (
    "README.md", "AGENTS.md", "START_HERE.md", "LEGAL.md",
    "MIGRATION_BACKLOG.md", "engine/geard-lif/README.md",
    "engine/geard-lif/SYSTEM_STATUS.md", "engine/geard-lif/UPSTREAM.json",
    "rules/RULES_INDEX.md", "rules/FOUNDATION.md", "rules/SKILLS.md",
    "rules/ADVANCEMENT.md", "rules/PERKS.md", "rules/DEFENSE.md",
    "rules/skills.json", "design/MAGIC.md", "design/PROGRESSION.md",
    "design/tes_perk_seeds.json", "lore/LORE_POLICY.md", "lore/ERAS.md",
    "game/CHARACTER_CREATION.md", "game/PRE_SESSION_PREP.md",
    "game/GM_PROTOCOL.md", "game/PERSISTENCE.md", "game/TEST_PLAN.md",
)
UPSTREAM_PAGES = (
    "Project_Framework", "Resource_Tracks",
    "Tentative_D10_Resolution", "Tentative_Tier_Scaling",
)
TEMPLATES = (
    "campaign.json", "character.json", "state.json", "world.json",
    "threads.json", "gm-secrets.json",
)
STATES = {"character_creation", "preparing", "active", "paused", "complete"}
MODELS = {"geard-lif-use-based"}


def _load_json(path: Path, errors: list[str]) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            errors.append(f"{path}: expected a JSON object")
            return {}
        return data
    except (OSError, ValueError) as exc:
        errors.append(f"{path}: {exc}")
        return {}


def validate_scaffold(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_DOCS:
        if not (root / rel).is_file():
            errors.append(f"missing document: {rel}")
    manifest = _load_json(root / "engine/geard-lif/UPSTREAM.json", errors)
    upstream = manifest.get("upstream_commit")
    if not isinstance(upstream, str) or not re.fullmatch(r"[0-9a-f]{40}", upstream):
        errors.append("Geard Lif upstream pin must be a full SHA")
    if manifest.get("source_repository") != "heatwaveqc/geard-lif":
        errors.append("unexpected mechanical upstream")
    for name in UPSTREAM_PAGES:
        path = root / "engine/geard-lif/source" / (name + ".tid")
        try:
            contents = path.read_text(encoding="utf-8")
        except OSError:
            errors.append(f"missing imported Geard Lif rule: {name}")
            continue
        if "geard-audience: player" not in contents.split("#",1)[0]:
            errors.append(f"imported rule must be player-audience only: {name}")
    skills = _load_json(root / "rules/skills.json", errors)
    if len(skills.get("skills", [])) != 24:
        errors.append("current Elf-Books roster must contain 24 candidate skills")
    perks = _load_json(root / "design/tes_perk_seeds.json", errors)
    if len(perks.get("items", [])) != 75:
        errors.append("TES perk inspiration catalog requires 75 entries")
    for name in TEMPLATES:
        path = root / "templates" / name
        item = _load_json(path, errors)
        if item and item.get("schema_version") != 1:
            errors.append(f"{name}: unsupported schema version")
        if name == "campaign.json":
            if item.get("status") != "character_creation":
                errors.append("campaign template must not be active")
            if item.get("engine",{}).get("id") != "geard-lif":
                errors.append("campaign template must use local Geard Lif")
            if item.get("engine",{}).get("upstream_commit") != upstream:
                errors.append("campaign upstream pin mismatch")
        if name == "character.json":
            if item.get("engine",{}).get("id") != "geard-lif":
                errors.append("character template must use Geard Lif")
            if "derived" in item or "magicka" in item or "attributes" in item:
                errors.append("legacy character template fields may not be active")
            if set(item.get("resources",{})) != {"mind","body","soul"}:
                errors.append("character must have three Geard resource aspects")
            for aspect,tracks in (("mind",("attention","plasticity")),
                                  ("body",("injury","fatigue")),
                                  ("soul",("mana","spirit"))):
                if any(item.get("resources",{}).get(aspect,{}).get(t) != [0,0,0,0] for t in tracks):
                    errors.append(f"character resource aspect missing four-grade track: {aspect}")
        if name == "gm-secrets.json" and item.get("preflight", {}).get("status") != "pending":
            errors.append("GM secrets template must not be ready")
    if (root / "campaigns").exists() or (root / "private-campaigns").exists():
        errors.append("public repo may not contain actual campaign storage")
    return errors


def _nonempty(value: object) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def validate_campaign(directory: Path) -> list[str]:
    errors: list[str] = []
    directory = directory.resolve()
    if directory == ROOT or ROOT in directory.parents:
        return ["private campaign files must not be stored in the public Elf-Books repository"]

    files = ("campaign.json", "state.json", "world.json", "threads.json", "gm/secrets.json")
    for rel in files:
        if not (directory / rel).is_file():
            errors.append(f"missing campaign file: {rel}")
    if errors:
        return errors

    campaign = _load_json(directory / "campaign.json", errors)
    state = _load_json(directory / "state.json", errors)
    world = _load_json(directory / "world.json", errors)
    _load_json(directory / "threads.json", errors)
    gm = _load_json(directory / "gm/secrets.json", errors)
    if errors:
        return errors

    cid = campaign.get("id")
    if not isinstance(cid, str) or not re.fullmatch(r"elf-[a-z0-9][a-z0-9-]{5,47}", cid):
        errors.append("invalid campaign ID (expected elf-... opaque slug)")
    if campaign.get("status") not in STATES:
        errors.append("unsupported campaign status")
    for name, obj in (("state", state), ("world", world), ("gm", gm)):
        if obj.get("campaign_id") != cid:
            errors.append(f"{name} campaign ID mismatch")

    char_dir = directory / "characters"
    character_files = list(char_dir.glob("*.json")) if char_dir.is_dir() else []
    if not character_files:
        errors.append("missing character files")
    for character_path in character_files:
        character = _load_json(character_path, errors)
        if character.get("campaign_id") != cid:
            errors.append(f"character campaign mismatch: {character_path.name}")

    event_path = directory / "events.jsonl"
    if not event_path.is_file():
        errors.append("missing events.jsonl")
    else:
        try:
            events = [json.loads(line) for line in event_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            nums = [e.get("seq") for e in events]
            if nums != list(range(1, len(events) + 1)):
                errors.append("event sequence is not consecutive from 1")
            if state.get("event_seq") != len(events):
                errors.append("state event_seq differs from public event log")
        except (OSError, ValueError, AttributeError) as exc:
            errors.append(f"events.jsonl invalid: {exc}")

    if campaign.get("status") in {"active", "paused", "complete"}:
        if not re.fullmatch(r"[0-9a-fA-F]{40}", str(campaign.get("rules_commit", ""))):
            errors.append("active campaign needs a pinned 40-character rules commit")
        setup = campaign.get("setup", {})
        if campaign.get("engine",{}).get("id") != "geard-lif":
            errors.append("active campaign must pin Geard Lif")
        if not re.fullmatch(r"[0-9a-fA-F]{40}", str(campaign.get("engine",{}).get("upstream_commit",""))):
            errors.append("active campaign must pin Geard Lif upstream commit")
        if setup.get("advancement", {}).get("model") not in MODELS:
            errors.append("active campaign requires an approved advancement model")
        if setup.get("session_zero", {}).get("approved") is not True:
            errors.append("active campaign requires approved session zero")
        for field in ("era", "date", "region"):
            if not _nonempty(setup.get(field)):
                errors.append(f"active campaign missing era/date/region: {field}")
        if gm.get("preflight", {}).get("status") != "ready":
            errors.append("GM preflight must be ready before activation")
        situation = gm.get("true_situation")
        if not _nonempty(situation):
            errors.append("private true situation is missing")
        spine = gm.get("campaign_spine", {})
        for field in ("central_conflict", "personal_stakes", "unopposed_outcome"):
            if not _nonempty(spine.get(field)):
                errors.append(f"campaign spine missing {field}")
        if len(spine.get("possible_resolutions", [])) < 2:
            errors.append("need at least two possible resolutions")
        opposition = gm.get("opposition", {})
        for field in ("identity", "goal", "means", "limitations"):
            if not _nonempty(opposition.get(field)):
                errors.append(f"opposition missing {field}")
        if len(opposition.get("conditional_moves", [])) < 3:
            errors.append("antagonist needs three conditional moves")
        for field, count in (
            ("factions", 2), ("npcs", 3), ("clocks", 1), ("locations", 3),
            ("near_horizon", 3), ("far_horizon", 2), ("revelations", 1),
        ):
            if len(gm.get(field, [])) < count:
                errors.append(f"GM preflight needs at least {count} {field}")
        clues = gm.get("clues", [])
        if len(clues) < 3 or len({c.get("id") for c in clues if isinstance(c, dict)}) < 3:
            errors.append("GM preflight needs three distinct clue IDs")
        methods = {c.get("method") for c in clues if isinstance(c, dict) and c.get("method")}
        if len(methods) < 2:
            errors.append("GM preflight needs at least two clue methods")
        opening = gm.get("opening", {})
        for field in ("inciting_incident", "why_now", "visible_change", "inaction"):
            if not _nonempty(opening.get(field)):
                errors.append(f"opening missing {field}")
        if len(opening.get("choices", [])) < 2:
            errors.append("opening needs at least two choices")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign", type=Path, help="validate an external/private campaign directory")
    args = parser.parse_args()
    errors = validate_campaign(args.campaign) if args.campaign else validate_scaffold()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: structural checks (NOT a playable-rules certification)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
