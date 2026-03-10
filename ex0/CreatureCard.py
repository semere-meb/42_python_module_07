from .Card import Card


class CreatureCard(Card):
    attack: int
    health: int

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': "Creature",
            'attack': self.attack,
            'health': self.health,
        }
        
    def play(self, game_state: dict) -> dict:
        return game_state
        
    def attack_target(self, target) -> dict:
        return {
            "attcker": self.name,
            'target': target.name,
            'damage_dealt': self.attack - target.attack,
            'combat_resolved': self.attack != target.attack,
        }
