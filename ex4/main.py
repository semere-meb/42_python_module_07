#! /usr/bin/env python3


from ex4 import TournamentCard, TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")

    tournament = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 10, "Legendary", "steal card")
    wizard = TournamentCard("Ice Wizard", 15, "Legendary", "do magic")

    for card in dragon, wizard:
        print()
        print(tournament.register_card(card))
        print("- Interfaces:", card.interfaces)
        print("- Rating:", card.rating)
        print("- Record:", f"{card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    print("Match result:", tournament.create_match(dragon.id, wizard.id))

    print("\nTournament Leaderboard...")
    leaderboard = tournament.get_leaderboard()
    for i in range(len(leaderboard)):
        card = leaderboard[i]
        print(f"{i+1}. {card.name} - Rating: {card.rating} ", end='')
        print(f"({card.wins}-{card.losses})")

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()
