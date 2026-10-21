"""Analyze 3.x-style D20 hit probabilities under Elf-Books AC alternatives.

Not operative game mechanics. Flat modifiers and optional AC baselines only.
"""
from dataclasses import dataclass


def modifier(ability_score: int) -> int:
    if type(ability_score) is not int:
        raise ValueError("ability score must be an integer")
    return (ability_score - 10) // 2


def hit_probability(attack_bonus: int, armor_class: int) -> float:
    if type(attack_bonus) is not int or type(armor_class) is not int:
        raise ValueError("attack bonus and AC must be integers")
    return sum(roll == 20 or (roll != 1 and roll + attack_bonus >= armor_class)
               for roll in range(1, 21)) / 20


@dataclass(frozen=True)
class Scenario:
    name: str
    attack_bonus: int
    defense_attribute: int
    defensive_skill: int
    armor: int = 0
    shield: int = 0
    natural_armor: int = 0

    def ac(self, base: int = 0) -> int:
        if base not in (0, 10):
            raise ValueError("choose base 0 or 10")
        if not 0 <= self.defensive_skill <= 100:
            raise ValueError("skill must be 0..100")
        return base + self.defense_attribute + self.defensive_skill // 5 + self.armor + self.shield + self.natural_armor

    def chance(self, base: int = 0) -> float:
        return hit_probability(self.attack_bonus, self.ac(base))


def archetypal_scenarios() -> list[Scenario]:
    a = modifier(25) + 20 + 5
    d = modifier(25)
    return [
        Scenario("full enchanted plate shield and natural armor",a,d,100,armor=13,shield=7,natural_armor=5),
        Scenario("enchanted plate and shield without natural armor",a,d,100,armor=13,shield=7),
        Scenario("unarmored, equal skill, no enchanted weapon", modifier(25)+20,d,100)
    ]


def main() -> None:
    for case in archetypal_scenarios():
        print(f"{case.name}: attack +{case.attack_bonus}; "
              f"AC no10={case.ac(0)} ({case.chance(0):.0%} hit), "
              f"AC with10={case.ac(10)} ({case.chance(10):.0%} hit)")


if __name__ == "__main__":
    main()
