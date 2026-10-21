# Actual damage skill XP, fivefold rank costs — calibration candidate

**Status: recommended trial, not yet the agreed operating XP rule.** Following the design discussion, test **actual effective HP loss** for offensive weapon XP, with five times the previous rank cost. Keep the already-agreed AC/armor risk mechanics in [DEFENSE.md](../rules/DEFENSE.md). This supersedes the **base weapon die XP** candidate in [XP_CALIBRATION.md](XP_CALIBRATION.md) as the preferred weapon experiment, but that earlier benchmark remains useful.

## Suggested formulas

```text
Skill rating s is an integer in 0..100.
XP required for next skill rank = 5 × max(1, s).  [candidate]
Offensive weapon XP per meaningful hit = actual HP removed from enemy by that weapon attack. [candidate]
```

**"Actual" means applied damage, not the rolled pre-resistance number.** For a simple attack, `xp = min(target_current_HP, max(0, rolled_damage - applicable_reduction))`. If a 45-damage strike hits a target with only 8 HP remaining, the attack can teach at most **8 XP** from that target, not 45. The attacker must legitimately hurt a target; empty-room swings and invulnerable targets grant no effective-damage XP. Do not conflate a missed attack with a zero-damage hit that might be eligible for some separate technique training.

This has a useful consequence: **total offensive damage XP available from killing a single enemy with 50 remaining HP is at most 50**, whether achieved with numerous dagger attacks or two huge sword strikes. High damage per action can still make XP/time or XP/turn faster, but not increase XP earned *per enemy killed*. No hidden weapon-die-specific multiplier is necessary. Wounds healed during a battle could permit more HP loss over time; that is also real repeated damage and an explicit economy to assess. No arbitrary penalty solely because a player deliberately chose dangerous practice.

Record awarded XP for the weapon attack's relevant rated skill (One-Handed, Two-Handed, Archery, Unarmed). **Potential split-source question:** if elemental enchantments, poison, reflected damage, summon attacks or triggered area effects cause some of the HP loss, decide whether those portions contribute to weapon, Destruction, Alchemy, Conjuration, or another skill. Do not automatically count a single HP as full experience for two skills. Critical damage and valid perk-enhanced damage are actual damage under this candidate, limited by target HP.

## Pacing comparison (ignoring missed attacks)

| Skill interval | Prior XP: K=1 | New XP: K=5 | Prior successful d8 hits (4.5 XP/hit) | New hits at 7.5 applied HP/hit | New hits at 14.5 applied HP/hit | New hits at 22.5 applied HP/hit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 20→25 | 110 | 550 | 24.4 | 73.3 | 37.9 | 24.4 |
| 50→55 | 260 | 1300 | 57.8 | 173.3 | 89.7 | 57.8 |
| 95→100 | 485 | 2425 | 107.8 | 323.3 | 167.2 | 107.8 |
| 20→100 | 4760 | 23800 | 1057.8 | 3173.3 | 1641.4 | 1057.8 |

Damage profiles are illustrative **actual HP loss per successful hit**, not unconditional 5e damage rolls: 7.5 is approximately 1d8+3; 14.5 is 1d8+7 ability+3 weapon; 22.5 is deliberately high. The number of successful hits depends on enemies actually having sufficient HP left; overkill and reductions lower the realized applied damage. The break-even rate between the old and new learning pace is **22.5 effective HP damage per successful d8 hit**. Early advancement may become much slower, despite the attractiveness of damage-based training at higher power.

**Encounter budget interpretation:** fighting one 50-HP enemy solo without outside damage/healing can award **at most 50 offensive XP**, regardless of attack count. Then 95→100 with K=5 needs at least 49 such enemies (2425 / 50 = 48.5), absent other XP sources. Against 100-HP foes it's at least 25. A build which wins fights faster earns the same XP per HP pool defeated in less combat time.

## Interaction with other skills

**The XP cost applies to *all* 0–100 skills** if we keep one universal rank ladder, so every award source must be reviewed with K=5 instead of blindly carrying the prior K=1 rates:

- **Heavy/Light Armor:** user's prior agreed principle remains: actual HP lost while wearing it earns armor experience even after a failed Block/Dodge. Trial 1 XP per actual HP loss now progresses very slowly at K=5; decide whether the faster weapon learning rate is deliberate, or set a higher armor multiplier after encounter testing. No free XP for artificial riskless simulated harm.
- **Block/Dodge:** the prevented threat's nominal damage may remain a good award unit, but must be tested with attack frequency, reaction limits and ability to defend without consuming a reaction after early perks.
- **Destruction and other magic:** if Destruction also learns from actual HP damage, area spells can earn multiple foes' HP in one cast. If non-damaging schools instead learn from Magicka used, spell cost ÷4 under K=5 is probably too small. Balance magic on time, limited resources, meaningful effects, and total outcome.
- **Restoration:** honest HP restored after real wounds may be comparable to armor HP loss, but casting limits and artificial wound loops need a conscious policy. There should be legitimate routes to learn nonharmful support magic.
- **Crafting/social/exploration:** the earlier 5/15/30/60 challenge awards were calibrated to K=1. With K=5, raise those benchmarks or adapt awards to the HP/stakes of the actual problem solved so an investigator or diplomat doesn't fall five times behind weapon training. Do not invent five checks where one genuinely decisive negotiation suffices.

## What to test next

1. Match offensive learning after 10–20 encounters for a novice (around skill 20), a specialist (50), and a master (95), comparing a light/dual-wield build and a heavy-hitting build **using attacks per turn and real hit rates**.
2. Hold enemy total HP fixed to test overkill, resistance, damage bonuses, multiple attacks and combat duration.
3. Run armor/Block/Dodge against the same attacks, measuring XP per *actual wound sustained* versus XP per *hit avoided* and remaining survival.
4. Run spellcaster damage, healing and utility with finite Magicka and meaningful noncombat progress, and compare session-to-session advancement.
5. Decide whether temporary HP, magical damage riders and damage-over-time are credited as damage dealt, and to which skill.

A 5× requirement and actual applied HP loss are an attractive **joint trial**, not separate automatic decisions. If the resulting early progression is too slow, a lower K or skill-dependent scale is simpler than creating hidden XP bonuses for every weapon.
