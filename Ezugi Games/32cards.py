import random

def play_32cards():
    deck = list(range(6, 14)) * 4  
    random.shuffle(deck)  

    players = {
        'Player 8': 8,
        'Player 9': 9,
        'Player 10': 10,
        'Player 11': 11
    }

    print("Starting cards for players:")
    for player, starting_card in players.items():
        print(f"{player}: {starting_card}")

    while True:
        for player in players:
            players[player] += random.choice(deck)

        print("\nTotal cards for players:")
        for player, total_card in players.items():
            print(f"{player}: {total_card}")

        max_value = max(players.values())
        winners = [player for player, value in players.items() if value == max_value]

        if len(winners) == 1:
            print(f"\n{winners[0]} wins!")
            break
        else:
            print("\nIt's a tie! Drawing another card for tied players.")

            tied_players = {player: players[player] for player in winners}
            for player in tied_players:
                tied_players[player] += random.choice(deck)
                print(f"{player} draws an additional card: {tied_players[player]}")

            players.update(tied_players)


if __name__ == "__main__":
    play_32cards()
