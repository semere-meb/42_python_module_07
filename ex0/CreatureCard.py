from .Card import Card


class CreatureCard(Card):
    attack: int
    health: int

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0:
            raise ValueError("CreatureCard can't have a negative attack")
        elif health < 0:
            raise ValueError("CreatureCard can't have a negative health")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health,
        }

    def play(self, game_state: dict) -> dict:
        game_state = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "No effect",
        }
        self.cost = 0
        return game_state

    def attack_target(self, target: Card) -> dict:
        return {
            "attcker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
