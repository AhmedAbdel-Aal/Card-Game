from card_game.card import Card
from card_game.game import Game


def test_tie_round_winner_takes_all():
    game = Game("Player 1", "Player 2")
    
    # Manually setting up the draw piles to control the outcome
    game.player_1.draw_pile = [Card(3), Card(1)]  # Player 1 will have a tie and then a lower card
    game.player_2.draw_pile = [Card(3), Card(2)]  # Player 2 will have a tie and then a higher card

    # Simulate the tied round
    game.play_turn()  # This should result in a tie with both players drawing the 3

    # Simulate the next round
    winner = game.play_turn()  # Player 2 should win with the 2 beating the 1

    # Verify Player 2 won the 4 cards
    assert winner is None  # No overall game winner yet
    assert len(game.player_2.discard_pile) == 4  # Player 2's discard pile should have 4 cards
    assert len(game.player_1.discard_pile) == 0  # Player 1's discard pile should be empty
    assert game.player_2.discard_pile == [Card(1), Card(2), Card(3), Card(3)]  # Verify the exact cards

    winner = game.play_turn()  # Player 2 should win with the 2 beating the 1
    assert winner is game.player_2
