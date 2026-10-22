# Private solo-campaign persistence — Geard Lif migration contract

Public Elf-Books includes reusable original lore, rules adapter, templates and tests **only**. Individual campaign state, GM secrets and private clocks live in an authorized **separate private repository/store**, never inside this public repo.

Proposed private structure remains:

```text
campaigns/<opaque-id>/
  campaign.json
  characters/<id>.json
  world.json
  threads.json
  state.json
  events.jsonl
  journal.md
  gm/secrets.json
  gm/private_events.jsonl
```

Every campaign pins a full **Elf-Books rules commit SHA**, **Geard upstream import SHA** and any adapter version. No engine auto-upgrades mid-campaign.

Character state (new schema, still under design) will have all twelve independently rated attributes, exactly one five-skill Talent with rating, chosen package ID or custom name, **no initial-Talent perk tree**, all 24 Skill ratings and their Specialties, Tiers, Health/Will/Conviction as attributes, six graded resource tracks (resilience and severity occupancy), Projects with Scope-sized **four-grade mark arrays**, Recalcitrance and Time, active Effects and Costs, inventory and perk awards. It will **not** contain D20 HP, fixed Magicka, six-ability-score-derived AC, or 0–100 rating assumptions.

Logs must preserve the **source category of every personal die** (Attribute/Talent/Skill/Specialty), each natural 10's separate Skill/Specialty bootstrap award, rating/XP bank before and after a roll, and the exact d10 faces, applied success convention, Tier conversion, resource marks/costs and changing world clocks for reproducibility and revalidation. One event ID grants progression/critical rewards only once. Save whole changed state coherently and read back a confirmed commit. Verify sequence continuity and correct authorized campaign before every write.

The pre-session private prep gate remains mandatory. A campaign may not become active until the actual engine, adaptation and save validator are ready. Existing D20 campaign saves are **not automatically migratable**; preserve the pinned D20 branch or explicitly plan an approved conversion and publish what changes on the sheet.

This is a specification, not evidence that private storage integrations already function.

**Trait-Tier ledger:** Tier-0 ratings remain in the base character trait fields. Additional per-trait Tier ratings are held under `trait_tiers` with explicit category/trait/Tier keys. XP banks are integer **tenths** of base XP, recording the destination trait and chosen Tier, source award, and whether it cascaded or remained for up-tier purchase. Passive event records include the actual chosen defense/Cost and participating traits, not invented defensive rolls. This addition is a schema contract, not a completed live campaign migration.

**Resource ownership, updated:** Mind/Will owns `spirit` (slow) and `mana` (fast). Soul/Conviction owns `plasticity` (slow) and `attention` (fast). Body/Health is unchanged. Do **not** migrate preexisting saved resource marks by changing object names in place; move each track's *entire existing mark array* to its new aspect, preserving its slow/fast identity, then reconcile capacity with the destination aspect's Resilience under an explicitly approved save migration. No live saves are migrated by this template change.

**Fivefold Tier migration:** before interpreting logged Tier 1+ events under the current rules, check which version produced their XP and cross-Tier magnitude. The adopted conversion is ×5 per Tier; historical ×10 results are not silently reinterpreted or overwritten. If old campaign saves exist, require an explicit migration decision. Fractional Tier 1+ passive XP is representable in the existing integer-tenths ledger.

**Resource overflow events:** preserve both `requested_resource` and `applied_resource` plus the overflow flag, original magnitude/Tier, destination's effective mark-grade threshold and resulting track arrays. Fast→slow redirection happens only if fast was **already exhausted before the event**. Do not silently invent an extra slow mark when the first hit exhausts fast, and do not redirect old recorded effects retroactively. When paying Mana Costs with saved state, provide both Mana **and** Spirit tracks so Spirit's existing marks are never silently reset.

**Perk ledger specification (adopted mechanics; implementation pending private store):** Maintain a character-wide bankable `perk_points` balance and purchased Skill perk IDs/ranks, with each perk's named Attribute, Skill, allowed Specialty group, composite threshold and any extra prerequisite documented. The initial Talent has **no perk tree**; later condition-linked vampire/werewolf perk purchases may require distinct progression fields. Each real rolled event preserves all original face sources (personal Attribute/Talent/Skill/Specialty vs equipment), the original face count of personal 10s/1s, the **exact one-shot confirmation faces** for acting character and targeted defender, the points each received, both recipient IDs and a unique **once-only event ID**. Confirmed 10s on personal dice earn actor points; attacker personal 1s confirmed as 1 earn defensive target points. **No source-equipment dice qualify** for either character perk bank, and confirmation dice do not create XP. Do not duplicate awards by replaying a saved event or by copying one attack's defensive 1s to every area target. Gear deed enchantments remain future design notes only.
