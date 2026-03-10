import random
from typing import List

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    cards: List[Card]

    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        card = [card for card in self.cards if card.name == card_name]
        if len(card) == 1:
            self.cards.remove(card[0])
            return True
        else:
            return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        card = random.choice(self.cards)
        self.remove_card(card.name)
        return card

    def get_deck_stats(self) -> dict:
        return {
            "total_cards":
                len(self.cards),
            "creatures":
                len([card for card in self.cards
                    if isinstance(card, CreatureCard)]),
            "spells":
                len([card for card in self.cards
                    if isinstance(card, SpellCard)]),
            "artifcats":
                len([card for card in self.cards
                    if isinstance(card, ArtifactCard)]),
            "avg_cost":
                sum([card.cost for card in self.cards]) / len(self.cards)
                if len(self.cards)
                else 0,
        }
