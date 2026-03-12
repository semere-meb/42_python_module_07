import random

from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    wins: int
    losses: int
    rating: int

    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 combat_type: str, **kwargs):
        super().__init__(
             name=name,
             cost=cost,
             rarity=rarity,
             combat_type=combat_type,
             **kwargs)
        self.id = self.name.split()[-1].lower() + \
            "_" + str(random.randint(0, 100))
        self.wins = 0
        self.losses = 0
        self.rating = random.randint(1000, 1500)
        self.interfaces = ["Card", "Combatable", "Rankable",]

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> dict:
        pass

    def defend(self, incoming_damage):
        pass

    def get_combat_stats(self):
        pass

    def get_rank_info(self):
        pass

    def update_wins(self, wins: int):
        pass

    def update_losses(self, losses: int):
        pass
