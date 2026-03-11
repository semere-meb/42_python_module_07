from abc import ABC, abstractmethod


class Card(ABC):
    name: str
    cost: int
    rarity: str

    def __init__(self, name: str, cost: int, rarity: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict: ...

    def get_card_info(self) -> dict:
        return {
            "Card": [
                "play",
                "get_card_info",
                "is_playable",
            ],
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana > 3
