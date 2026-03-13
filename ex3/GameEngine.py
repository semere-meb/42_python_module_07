from __future__ import annotations

from typing import Optional

from .GameStrategy import GameStrategy
from .CardFactory import CardFactory


class GameEngine:
    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None
        self._turns_simulated = 0
        self._total_damage = 0
        self._last_actions: dict = {}

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy):
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        if self._factory is None or self._strategy is None:
            raise RuntimeError("GameEngine not configured correctly")

        deck = self._factory.create_themed_deck(3)
        hand = []
        for subset in deck.values():
            hand.extend(subset)

        enemy_targets = ["Enemy Player", "Enemy Creature"]

        actions = self._strategy.execute_turn(hand, enemy_targets)

        self._turns_simulated += 1
        self._total_damage += actions.get("damage_dealt", 0)
        self._last_actions = actions

        report = {
            "turns_simulated": self._turns_simulated,
            "strategy_used": self._strategy.get_strategy_name(),
            "total_damage": self._total_damage,
            "cards_created": len(hand),
        }

        return report

    def get_engine_status(self) -> dict:
        return {
            "factory": type(self._factory).__name__ if self._factory else None,
            "strategy": type(self._strategy).__name__
            if self._strategy else None,
            "supported_types": self._factory.get_supported_types()
            if self._factory
            else {},
        }
