from abc import ABC, abstractmethod


class Combatable(ABC):
    combat_type: str

    def __init__(self, combat_type: str, **kwargs):
        super().__init__(**kwargs)
        self.combat_type = combat_type

    @abstractmethod
    def attack(self, target) -> dict: ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict: ...

    @abstractmethod
    def get_combat_stats(self) -> dict: ...
