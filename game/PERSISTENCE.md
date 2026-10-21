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

Character state (new schema, still under design) will have all twelve independently rated attributes, exactly one five-skill Talent with rating, chosen package ID or custom name, Talent-tree progression, all 24 Skill ratings and their Specialties, Tiers, Health/Will/Conviction as attributes, six graded resource tracks (resilience and severity occupancy), Projects with Scope-sized **four-grade mark arrays**, Recalcitrance and Time, active Effects and Costs, inventory and perk awards. It will **not** contain D20 HP, fixed Magicka, six-ability-score-derived AC, or 0–100 rating assumptions.

Logs must preserve the **source category of every personal die** (Attribute/Talent/Skill/Specialty), each natural 10's separate Skill/Specialty bootstrap award, rating/XP bank before and after a roll, and the exact d10 faces, applied success convention, Tier conversion, resource marks/costs and changing world clocks for reproducibility and revalidation. One event ID grants progression/critical rewards only once. Save whole changed state coherently and read back a confirmed commit. Verify sequence continuity and correct authorized campaign before every write.

The pre-session private prep gate remains mandatory. A campaign may not become active until the actual engine, adaptation and save validator are ready. Existing D20 campaign saves are **not automatically migratable**; preserve the pinned D20 branch or explicitly plan an approved conversion and publish what changes on the sheet.

This is a specification, not evidence that private storage integrations already function.

**Trait-Tier ledger:** Tier-0 ratings remain in the base character trait fields. Additional per-trait Tier ratings are held under `trait_tiers` with explicit category/trait/Tier keys. XP banks are integer **tenths** of base XP, recording the destination trait and chosen Tier, source award, and whether it cascaded or remained for up-tier purchase. Passive event records include the actual chosen defense/Cost and participating traits, not invented defensive rolls. This addition is a schema contract, not a completed live campaign migration.
