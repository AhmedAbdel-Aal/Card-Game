from unittest.mock import patch
from card_game.player import Player
from card_game.card import Card

@patch('card_game.player.FisherYates')
def test_reshuffle_discard_into_draw(mock_fisher_yates):

    mock_fisher_yates.return_value = [Card(3), Card(1), Card(2)]
    
    player = Player("Test Player")
    player.discard_card(Card(1))
    player.discard_card(Card(2))
    player.discard_card(Card(3))

    assert len(player.draw_pile) == 0
    assert len(player.discard_pile) == 3
    
    drawn_card = player.draw_card()  # This should trigger the reshuffle
    
    mock_fisher_yates.assert_called_once()
    assert len(player.draw_pile) == 2  # One card is drawn, so two should remain
    assert len(player.discard_pile) == 0
    assert drawn_card.value == 3  # Assuming the mock returns [Card(3), Card(1), Card(2)]