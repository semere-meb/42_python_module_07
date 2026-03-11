from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self, name: str,
        cost: int,
        rarity: str,
        combat_type: str,
        mana: int,
        **kwargs,
    ):
        super().__init__(
            name=name,
            cost=cost,
            rarity=rarity,
            combat_type=combat_type,
            mana=mana,
            **kwargs,
        )

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": target.cost,
            "combat_type": self.combat_type,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        result = {
            "caster": self.name,
            "spell": spell_name,
            "targets": [target.name for target in targets],
            "mana_used": self.mana,  # TODO: not all mana
        }
        self.mana -= self.mana
        return result

    # Combatable
    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        return {
            "Combatable": ["attack", "defend", "get_combat_stats"],
        }

    # Magical
    def channel_mana(self, amount: int) -> dict:
        res = {"channeled": amount, "total_mana": self.mana - amount}
        self.mana -= amount
        return res

    def get_magic_stats(self) -> dict:
        return {
            "Magical": ["cast_spell", "channel_mana", "get_magic_stats"],
        }
