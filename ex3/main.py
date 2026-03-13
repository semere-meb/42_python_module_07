#! /usr/bin/env python3

from ex3 import GameEngine, FantasyCardFactory, AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("\nConfiguring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    status = engine.get_engine_status()
    print("\nFactory:", status.get("factory"))
    print("\nStrategy:", status.get("strategy"))
    print("\nAvailable types:", status.get("supported_types"))

    print("\nSimulating aggressive turn...")

    # Show a sample hand (recreate the initial hand for display purposes)
    deck = factory.create_themed_deck(3)
    hand = []
    for subset in deck.values():
        hand.extend(subset)

    print("Hand:", [f"{card.name} ({card.cost})" for card in hand])

    report = engine.simulate_turn()

    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", engine._last_actions)

    print("\nGame Report:")
    print(report)


if __name__ == "__main__":
    main()
