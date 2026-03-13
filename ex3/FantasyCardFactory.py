import random
from typing import Any

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creature_templates = {
            "dragon": {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": "Legendary",
                "attack": 5,
                "health": 5,
            },
            "goblin": {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": "Common",
                "attack": 2,
                "health": 2,
            },
        }

        self._spell_templates = {
            "fireball": {
                "name": "Fireball",
                "cost": 3,
                "rarity": "Rare",
                "effect_type": "fire",
            },
            "lightning": {
                "name": "Lightning Bolt",
                "cost": 3,
                "rarity": "Rare",
                "effect_type": "lightning",
            },
        }

        self._artifact_templates = {
            "mana_ring": {
                "name": "Mana Ring",
                "cost": 2,
                "rarity": "Uncommon",
                "durability": 3,
                "effect": "mana boost",
            },
            "ancient_staff": {
                "name": "Ancient Staff",
                "cost": 4,
                "rarity": "Epic",
                "durability": 5,
                "effect": "spell power",
            },
        }

    def create_creature(self, name_or_power:
                        str | int | None = None) -> CreatureCard:
        if (
            isinstance(name_or_power, str)
            and name_or_power.lower() in self._creature_templates
        ):
            template = self._creature_templates[name_or_power.lower()]
        elif isinstance(name_or_power, int):
            template = min(
                self._creature_templates.values(),
                key=lambda t: abs(t["cost"] - name_or_power),
            )
        else:
            template = random.choice(list(self._creature_templates.values()))

        return CreatureCard(
            template["name"],
            template["cost"],
            template["rarity"],
            template["attack"],
            template["health"],
        )

    def create_spell(self, name_or_power:
                     str | int | None = None) -> SpellCard:
        if (
            isinstance(name_or_power, str)
            and name_or_power.lower() in self._spell_templates
        ):
            template = self._spell_templates[name_or_power.lower()]
        elif isinstance(name_or_power, int):
            template = min(
                self._spell_templates.values(),
                key=lambda t: abs(t["cost"] - name_or_power),
            )
        else:
            template = random.choice(list(self._spell_templates.values()))

        return SpellCard(
            template["name"],
            template["cost"],
            template["rarity"],
            template["effect_type"],
        )

    def create_artifact(self, name_or_power:
                        str | int | None = None) -> ArtifactCard:
        if (
            isinstance(name_or_power, str)
            and name_or_power.lower() in self._artifact_templates
        ):
            template = self._artifact_templates[name_or_power.lower()]
        elif isinstance(name_or_power, int):
            template = min(
                self._artifact_templates.values(),
                key=lambda t: abs(t["cost"] - name_or_power),
            )
        else:
            template = random.choice(list(self._artifact_templates.values()))

        return ArtifactCard(
            template["name"],
            template["cost"],
            template["rarity"],
            template["durability"],
            template["effect"],
        )

    def create_themed_deck(self, size: int) -> dict:
        types = ["creature", "spell", "artifact"]
        deck: dict[str, list[Any]] = {
            "creatures": [],
            "spells": [],
            "artifacts": [],
        }

        for _ in range(size):
            kind = random.choice(types)
            if kind == "creature":
                deck["creatures"].append(self.create_creature())
            elif kind == "spell":
                deck["spells"].append(self.create_spell())
            else:
                deck["artifacts"].append(self.create_artifact())

        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self._creature_templates.keys()),
            "spells": list(self._spell_templates.keys()),
            "artifacts": list(self._artifact_templates.keys()),
        }
