# Solo-chat progression pacing comparison (25,000 seeded trials per mode)

**Status:** Simulation evidence only. Rank cost `5×current skill` and `2 XP per actual offensive HP damage` are agreed; quick-check `2×DC / 0.5×DC` and extended-progress `1 XP per 10 progress` are **candidate** rates. See [generalized XP design](GENERALIZED_EXTENDED_XP.md) and [reproducible simulator](../scripts/pacing_comparisons.py).

## Why player time and fictional time must be separated

In this solo AI-GM environment, one chat exchange can encompass one round of combat (around six fictional seconds), one quick skill challenge, **or months of substantive crafting and downtime**. The latter must still resolve the underlying work intervals, resource costs, failure consequences, NPC clocks and accumulated progress; a short summary does not mean those events never happened.

**Therefore compare (1) chat/player decisions; (2) fictional weeks elapsed; and (3) risk, materials and genuine work accomplished.** Trying to give combat and crafting equal XP per *in-world minute* would make downtime absurdly slow, whereas equal XP per *message* would punish all lengthy projects.

## Explicit test assumptions

Simulated 25,000 attempts per skill band per mode, with seeded uniform real d20 and damage-die samples (simulated dice for research, not player-session rolls).

| Starting skill | Ability mod | Attack skill bonus | Magic weapon | Enemy HP | Quick/project DC | Project goal |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 20 | +3 | +4 | +0 | 35 | 15 | 1,000 |
| 50 | +5 | +10 | +0 | 60 | 25 | 2,500 |
| 95 | +7 | +19 | +3 | 110 | 40 | 6,000 |

- **Combat:** One 1d8 weapon attack per chat combat exchange, 60% hit chance including a 5% natural-20 critical adding another d8. Damage = 1d8 + ability + skill/5 + optional magic. XP = 2×actual enemy HP lost, after capping overkill at remaining HP. A fresh same-HP enemy is available immediately; no travel, healing, reaction, spell, bonus attacks, multiple enemies or injuries are modeled. These are optimistic combat conditions.
- **Quick:** One consequential static-DC roll per chat exchange. Full 2×DC XP on success, 0.5×DC on genuine failure; success probabilities 65%, 55%, 35% at the three skill bands. No free repeated impossible checks.
- **Extended:** One real weekly interval at project DC. Success credits `min(remaining_goal, check_total×DC)` progress; failed intervals credit none. XP = actual credited progress / 10, paid incrementally. A *single player-facing chat exchange* may summarize all intervals needed to finish **one** project. Separate project exchanges include any partly completed final project. Materials and downtime costs are not numerically charged in the simulation.

### Expected five-skill-point pacing

| Skill increase | XP needed | Combat: chat attacks | Quick: chat checks | Project: chat summaries | Project: fictional weekly intervals |
| --- | ---: | ---: | ---: | ---: | ---: |
| 20→25 | 550 | **~45** | **~26** | **6** | **~32 weeks** |
| 50→55 | 1,300 | **~63** | **~40** | **6** | **~38 weeks** |
| 95→100 | 2,425 | **~74** | **~60** | **5** | **~49 weeks** |

For those combat examples, approximately 27/38/44 hits land on roughly 8/11/12 opponents (whole or partial HP pools); **overkill wastes theoretical damage XP**, so attack exchanges are higher than optimistic unbounded damage calculations.

### Holding project scope constant

If every artisan instead completes **the same 1,000-progress project** repeatedly, the proposed scalar yields 100 XP per finished project:

| Starting rank | Project chat summaries for +5 | Weekly work intervals |
| --- | ---: | ---: |
| 20 | 6 | ~32 |
| 50 | 13 | ~47 |
| 95 | 25 | ~72 |

Thus the faster *chat* progress at higher skill in the first comparison is contingent upon choosing larger, harder, appropriately substantial projects (1,000/2,500/6,000 progress), not simply owning a higher Smithing skill.

## Interpretation

- **Yes, crafting and research can advance drastically faster per chat exchange. That is appropriate if months genuinely pass.** It is not gratis advancement. The player spent weeks of character time, materials, supplies, wages, space, connections and exposure to NPC/world events.
- **Quick check advancement is comparatively close to combat on the chat-message axis**, under the two tentative DC reward rates. A thief/investigator can advance through active adventure without needing multiple rolls for every fictional sentence.
- **Five ranks in roughly a fictional year of regular advanced crafting is a plausible outcome**, not a command that every character must spend 49 uninterrupted weeks. Real-world pauses and project scale matter.
- **Project XP is not intrinsically per chat message.** One player can batch projects into a single request; another can spend multiple chats making decisions during one project. Any mandated "one XP reward per exchange" would be artificial and easy to manipulate. XP should attach to **work actually completed and choices made**, not the text interface.
- **Keep 1 XP per 10 credited progress as a trial** while building actual recipes, project/contract costs and world clocks. Halving or doubling that scalar roughly doubles or halves the required amount of real work, but cannot force an invariant chat-turn rate.
- Guard against impossible quick-check failures farming `0.5×DC`. Failures must represent authentic effort with a feasible challenge, not an arbitrarily elevated or impossible DC.
- The user approves deliberate real risk for armor learning; do not insert artificial safety caps just to equalize activities.

## Sources and limitations

D20 rounds take approximately six seconds ([D&D 5e basic rules](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat)). D&D 3.5 Craft uses DC×check-total weekly progress in silver, or daily in copper ([3.5 SRD Craft](https://www.d20srd.org/srd/skills/craft.htm)); Elf-Books uses fixed predeclared abstract progress units and intervals.

The simulator omits total character survivability, actual adversary skill and tactics, check retry costs, enchantment/alchemy material economies, and skill XP from other roles in a fight. Results **do not constitute a balanced or playable campaign**.
