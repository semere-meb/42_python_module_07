from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard

from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        max_mana = 5
        mana_used = 0
        cards_played = []
        damage_dealt = 0

        playable_cards = sorted(hand, key=lambda c: getattr(c, "cost", 0))

        for card in playable_cards:
            if mana_used + getattr(card, "cost", 0) > max_mana:
                continue

            cards_played.append(card.name)
            mana_used += getattr(card, "cost", 0)

            if isinstance(card, CreatureCard):
                damage_dealt += getattr(card, "attack", 0)
            elif isinstance(card, SpellCard):
                damage_dealt += getattr(card, "cost", 0) * 2

            card.play({})

        targets = self.prioritize_targets(battlefield)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            return []

        prioritized = [
            t for t in available_targets if "player" in str(t).lower()
        ]
        prioritized += [t for t in available_targets if t not in prioritized]

        return prioritized[:3]
