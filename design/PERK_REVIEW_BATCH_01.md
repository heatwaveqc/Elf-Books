# Perk review batch 01 — first five in the catalogue

**STATUS: USER REVIEW REQUESTED, NOT ADOPTED.** This document proposes final gates and ranked alternatives, without changing the three previously adopted combat pilot effects. The user has adopted the *general* rankable-perk mechanic, the fixed external-equipment cap (perk dice do not increase it), and the choice between an explicit named Specialty list versus **Any Specialty of the named Skill**. Those framework rules live on Elf Books main in [Perks](../rules/PERKS.md). See [entire draft](PERK_CATALOG_DRAFT.md).

## Shared review convention

The stated requirement is the combined rating of **the named Attribute + named Skill + initial Talent only when governing that Skill + one actual accepted Specialty**. Where a perk says **Any**, it means any real Specialty *belonging to that Skill*, not a Specialty from another Skill. Perks with multiple ranks have to be purchased one rank at a time, normally one bankable perk point per rank, and meet each new rank's requirement.

**Every perk-granted rolled die is Skill-equivalent for XP and actor confirmed-10 / defender confirmed-attacker-1 perk points**. Its roll provenance is `perk_skill`, and it does not increase the rated personal pool used as the cap for gear/magic external bonuses. The specific attack still pays its ordinary self-Fatigue hazard in addition to extra hazard listed by a perk.

## 1. Critical Charge — One-Handed (consider five ranks)

**Proposed purchase gate:** **Strength + One-Handed**, **Any One-Handed Specialty**. Existing one-rank draft gate: **50**. Proposed five-rank alternative: **50 / 60 / 70 / 80 / 90**, for +1d to +5d damage on an actual qualifying charge.

**Operation:** On your turn, spend an ordinary movement action to move from outside melee into the attack's legal reach of a real opponent; then spend a separate ordinary attack action against that opponent **immediately after that move**. Before the attack attempt, choose up to your purchased charge rank in extra Potence damage dice. Resolve the attack normally. Add **one Fatigue hazard die per chosen bonus die** to that attempted attack even on a miss. This does not make the movement free, and the modifier is used for *the next attempt*, not saved until the next hit. Unused movement or standing still does not qualify. Whether the actual rolled movement distance must exceed a minimum and whether the extra dice should also be capped by Strength dice are **open balancing choices**.

**Reviewer decisions:** Keep 50 as first gate or lower it? Adopt 5 charge ranks or preserve the earlier +2d, one-rank maneuver? If ranked, choose +1d Fatigue hazard per extra damage die (proposal) or Power Bash's stronger +2d/die? Do **Armsman** and **Critical Charge** bonus dice stack on the same strike? This is the clearest cross-perk stacking decision for the first batch.

## 2. Dual Flurry — One-Handed (one rank; previously adopted effect)

**Proposed purchase gate:** **Dexterity + One-Handed, 30**, with **Any One-Handed Specialty**. Alternative: explicit **Dual Wielding Specialty** for more gated thematic commitment, possibly raising the threshold to **50 or 60**; neither is adopted.

**Operation (already approved):** When holding two ready melee weapons, one ordinary attack action generates **two sequential, independent full-strength strikes**, one per weapon, each using its own legal Accuracy and successful-hit Potence dice, with an independent normal attempted-attack Fatigue Cost **even if it misses**. Effects and accumulating marks from the first attempt apply before the second. You may spend the other two actions on attacks too, yielding up to six strikes per round. No extra reactions/movement/free Cost mitigation.

**Reviewer decisions:** Does the original low gate 30 correctly reflect how powerful the action-economy gain is? Is Any One-Handed Specialty enough, or should a named Dual Wielding Specialty be necessary? The effect itself is **not** reopened by this review unless explicitly requested.

## 3. Hack and Slash — One-Handed (five ranks; recurring Injury Hazard)

**Proposed rank gates:** **Strength + One-Handed**, with an **actually possessed and applicable Axes/Hatchets Specialty required at every rank** (not merely optional bonus dice), at total rating **30 / 45 / 60 / 75 / 90**. Purchase consecutively, one bankable perk point per rank.

| Purchased rank | Minimum composite prerequisite | Recurring Injury Hazard |
| --- | ---: | ---: |
| 1 | 30 | **1d10** |
| 2 | 45 | **2d10** |
| 3 | 60 | **3d10** |
| 4 | 75 | **4d10** |
| 5 | 90 | **5d10** |

**Trigger:** An actual axe/hatchet hit must cause at least **one Middling-or-worse Injury mark** after the ordinary attack's Potence, armor, and other protections. Smaller wounds do not start bleeding. The weapon/target must be capable of physically bleeding. Initial Injury and the attacker's attempted-attack Fatigue Cost are resolved normally; this perk adds a lasting **bleeding condition**, not an automatic extra Injury mark on initial contact.

**Ongoing hazard:** Starting at the **beginning of the victim's next own turn**, and once at the beginning of each of their later turns while the bleed remains active, roll a fresh **rank d10 Injury Hazard**, using the ordinary face-to-success map (1–6 = 0, 7–9 = 1, 10 = 2). It is an **independent new Injury incident** each turn with no new Accuracy/application roll and no extra attacker action/Cost. Grade and apply the rolled successes against the target's **unmodified Health-derived Injury threshold and mark capacity, without Armor Rating**. Armor protected the triggering strike; it does not seal an already opened blood vessel. Health and legitimate *nonarmor* intrinsic bleed resistance still apply where actually defined. The target cannot Dodge, Block, or Parry the continuing loss of blood.

**Ends on full resistance:** If that turn's Injury Hazard causes **no Injury mark**, the bleeding condition ends immediately. With the existing Geard Lif positive-magnitude grading rule, a hazard whose dice produce **zero successes** causes no mark and therefore ends the bleed; a positive magnitude causes at least a Minor mark against ordinary positive Health, even if it is below the Middling threshold. Healing the already recorded Injury marks is separate from stopping the bleeding condition unless a specific treatment or power says otherwise.

**Nonstacking:** A target can have **at most one active Hack and Slash bleed**. A subsequent qualifying axe strike may replace a lower bleed rank with a higher one, not create an additional independent hazard; equal/lower ranks do not restart or multiply it. If the condition has already ended, a later genuine qualifying strike may begin a new one.

**Mathematical balance warning:** At rank `r`, if ending requires a 0-success hazard, the chance to stop on any tick is `0.6^r`. At rank 1, **60%** of ticks end the bleed without Injury, but at rank 5 only **7.776%** do. With independent unchanged rolls, the expected number of **damaging ticks before the first zero-success tick** is `(1-0.6^r)/(0.6^r)`: about **0.67 at rank 1** versus **11.86 at rank 5**. Even though hazard dice grow linearly, bleed duration and total harm grow very sharply. This is a purposeful design stress test, not yet proof that rank 5 is balanced.

**Experience/confirmation question:** User-approved general rule credits **rolled bonus dice granted to a character's Skill pool** as Skill dice for XP and double-10/attacker double-1 perk confirmations. An independently ticking **bleeding hazard** is not literally another attack/Skill roll made by the original attacker. **Proposed distinction for review:** tag autonomous ticks as `bleeding_hazard` rather than `perk_skill` and give them no new Skill XP or perk confirmations; the **original axe attack's actual perk-enhanced Skill dice** remain eligible as usual. This prevents passive XP farming without weakening the user-approved rule for actual perk-created Skill dice. If the user intends *all* dice produced by a perk, even unattended hazards, to train a character, that broader interpretation should be approved explicitly before activation.

**Remaining narrow blockers:** confirming what counts as bleed-capable anatomy; exact start-of-turn ordering and how actual healing/bandaging/Restoration can staunch bleeding; and the status of passive hazard rolls for XP. The ranked dice, trigger, armor bypass, independent new hazard roll, nonstacking, and end-on-no-Injury procedure are directly specified.

## 4. Armsman — One-Handed (consider five ranks)

**Proposed purchase gate:** **Strength + One-Handed**, **Any One-Handed Specialty**. Earlier flat one-rank draft gate: **0**. Proposed five-rank alternative: **0 / 25 / 50 / 75 / 90**.

**Operation:** Before each muscle-powered One-Handed attack attempt, choose **0 through owned Armsman rank** additional Potence damage dice. Raise the ordinary attempted-attack Fatigue hazard by **one die per bonus damage die**, even on a miss. The weapon's printed Damage rating does not change. All extra rolled faces are `perk_skill` for XP and breakthroughs. This is a general voluntary power attack, not a passive always-on permanent item damage increase. An ordinary 0d gear-hazard attack still has the chosen extra Armsman hazard.

**Reviewer decisions:** Is rank 1 at threshold 0 acceptable because it still costs a perk point? Should rank 5 need 90 or 100? Do the damage and hazard increments line up (proposed +1d/+1d, versus Power Bash's +1d/+2d)? Decide how Armsman stacks with charge, Finesse, Backstab and other perks that modify the same Potence roll. Any total perk bonus cap should be explicit, not silently conflated with the gear cap.

## 5. Sweep — Two-Handed (one rank; needs attack geometry)

**Proposed purchase gate:** **Strength + Two-Handed, 70**, **Any Two-Handed Specialty**. The current draft instead lists Greatswords, Battleaxes, Warhammers and Polearms; the permissive Any version must **still** require a held weapon and actual adjacent targets in a credible sweeping arc.

**Operation:** Spend **one** attack action to deliver up to **two sequential strikes against two DISTINCT enemies** who are within a real reachable sweep arc. For each target make a separate Accuracy roll and a Potence roll if that Application succeeds; pay each attempted strike's normal weapon Fatigue hazard (one incident per strike), even on a miss. Resolve changes/penalties between strikes. This is a multi-target action, not two hits on the same target and not an automatic full-circle Area attack.

**Reviewer decisions:** Keep two victims per use or allow a higher-rank progression for more? Should every Two-Handed weapon be able to Sweep if targets are positioned plausibly, or should some (e.g., a long polearm) require a particular attack mode? Geometry/reach and shared attack event handling need a narrow test before the perk becomes operative.

## Additional five-rank Finesse and Power Bash review candidates (not counted as first five)

- **Finesse:** proposed five gates **20 / 40 / 60 / 75 / 90**; ranks 1–4 may add **up to 1/2/3/4 ACTUALLY ROLLED bonus Potence d10**, subject to having that many surplus Accuracy successes; **rank 5 removes the rank cap** but never creates successes without rolled dice or without actual Accuracy margin. Its bonus faces earn Skill XP/confirmed perk points and do not raise self-Fatigue hazard or the external equipment cap.
- **Power Bash:** proposed five ranks, each permits one additional Damage die, still bounded by **Strength dice**, with **2 extra Fatigue hazard dice per chosen Damage die**, payable on miss. A possible threshold ladder is **30 / 45 / 60 / 75 / 90**. Its *existing adopted effect* still permits up to Strength dice while specific ranked restrictions are being reviewed; this draft does not secretly impose new limitations before approval.

## Approval checkpoint

**Already adopted (not up for redefinition without request):** one general perk point bank, Skill-equivalent training and confirmation on perk bonus dice, no effect of perk dice on the gear bonus allowance, sequential-rank infrastructure, wildcard Specialty matching, and Dual Flurry's effect.

**Candidate choices to ratify in this batch:** Charge/Armsman ranks and costs; five numeric gate sets; each allowed Specialty set; actual bleeding procedure; Sweep attack geometry; and especially **whether multiple damage-boosting perks can apply to the same attack**.

Do not mark these five fully purchased/implemented from this note alone.
