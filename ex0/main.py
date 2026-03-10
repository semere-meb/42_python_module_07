#! /usr/bin/env python3


from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    try:
        cc = CreatureCard("Fire Dragon", 6, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 10, "Legendary", 3, 5)
    except ValueError:
        print("Error creating a card. Stopping now")
        return
    print("\nCreatureCard Info:")
    print(cc.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", cc.is_playable(6))
    game_state = {
        "card_played": "Fire Dragon",
        "mana_used": 5,
        "effect": "Creature Summoned to battlefield",
    }
    print("Play result:", cc.play(game_state))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", cc.attack_target(goblin))

    print("\nTesting insufficient mana (3 available)")
    print("Playable:", cc.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
