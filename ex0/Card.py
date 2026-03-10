from abc import ABC, abstractclassmethod


class Card(ABC):
    name: str
    cost: int
    rarity: str

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractclassmethod
    def play(self, game_state: dict) -> dict: ...

    def get_card_info(self) -> dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        return {"Playable": available_mana > 3}
