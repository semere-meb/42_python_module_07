from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard

from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a single aggressive turn.

        Plays the lowest-cost cards first until mana is exhausted. Damage is
        computed using creature attack values and spell effects.
        """
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

            # Apply a simple damage formula based on card type
            if isinstance(card, CreatureCard):
                damage_dealt += getattr(card, "attack", 0)
            elif isinstance(card, SpellCard):
                # Spells deal damage proportional to their cost (simple proxy)
                damage_dealt += getattr(card, "cost", 0) * 2

            # Simulate playing the card (may mutate card state)
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
        """Prioritize targets by ranking them (player first, then creatures)."""
        if not available_targets:
            return []

        # Ensure consistent ordering: player first, then any other targets.
        prioritized = [t for t in available_targets if "player" in str(t).lower()]
        prioritized += [t for t in available_targets if t not in prioritized]

        # Limit targets to a reasonable number
        return prioritized[:3]
