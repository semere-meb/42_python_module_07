from ex0.Card import Card


class SpellCard(Card):
    effect_type: str

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type,
        }
        self.cost = 0
        return game_state

    def resolve_effect(self, targets: list) -> dict:
        return {
            "targets": targets,
        }
