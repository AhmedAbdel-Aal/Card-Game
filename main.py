from card_game.game import Game

def main():
    game = Game("Player 1", "Player 2")
    game.setup_game()
    
    winner = None
    while not winner:
        winner = game.play_turn()
    
    print(f"{winner.name} wins the game!")


if __name__ == "__main__":
    main()