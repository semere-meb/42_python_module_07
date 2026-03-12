import random
from typing import List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    matches_played: int
    cards: List[TournamentCard]
    status: str

    def __init__(self) -> None:
        self.cards = []
        self.matches_played = 0
        self.status = 'active'

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        return f"{card.name} (ID: {card.id})"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = [card for card in self.cards if card.id == card1_id][0]
        card2 = [card for card in self.cards if card.id == card2_id][0]
        players = [card1, card2]
        winner = random.choice(players)
        winner.wins += 1
        winner.rating += 16
        players.remove(winner)
        loser = players[0]
        loser.losses += 1
        loser.rating -= 16
        self.matches_played += 1
        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        return sorted(self.cards, key=lambda x: x.rating, reverse=True)

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating":
                sum([card.rating for card in self.cards])/len(self.cards)
                if len(self.cards)
                else 0,
            "platform_status": self.status,
        }
