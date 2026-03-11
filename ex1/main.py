#! /usr/bin/env python3


from ex0.CreatureCard import CreatureCard

from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck different card types...")
    deck = Deck()
    cards = [
        ArtifactCard("Mana Crystal", 10, "rare", 5,
                     "Permanent: +1 mana per turn",),
        CreatureCard("Random Creature", 10, "Legendary", 10, 10),
        SpellCard("Lightning Bolt", 10, "Rare", "Deal 3 damage to target"),
    ]

    for card in cards:
        deck.add_card(card)
    print("Deck stats:", deck.get_deck_stats())

    game_state = {}
    for i in range(2):
        card = deck.draw_card()
        print("\nDrew:", card.name, f"({type(card).__name__})")
        print("Play result:", card.play(game_state))

    print("\n Ploymorphism in action: Same interface," +
          " different card behavriors!")


if __name__ == "__main__":
    main()
