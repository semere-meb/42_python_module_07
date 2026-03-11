from ex2 import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    ec = EliteCard("Arcane Warrior", 10, "Legendary", "melee", 20)
    target = EliteCard("Enemy", 10, "Legendary", "random", 5)
    target1 = EliteCard("Enemy1", 10, "Legendary", "random", 7)
    target2 = EliteCard("Enemy2", 10, "Legendary", "random", 3)
    print("-", ec.get_card_info())
    print("-", ec.get_combat_stats())
    print("-", ec.get_magic_stats())

    print(f"\nPlaying {ec.name} ({type(ec).__name__})")

    print("\nCombat Phase:")
    print("Attack result:", ec.attack(target))

    print("\nMagic phase:")
    print("Spell cast:", ec.cast_spell("Fireball", [target1, target2]))
    print("Mana channel:", ec.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
