from card_game.deck import Deck
from unittest.mock import patch

def test_new_deck_contains_40_cards():
    """
    A new deck should contain 40 cards
    """
    deck = Deck()
    assert len(deck.cards) == 40

def test_draw_card():
    deck = Deck()
    card = deck.draw_card()
    assert len(deck.cards) == 39
    assert card is not None


@patch('card_game.deck.FisherYates')
def test_shuffle_function_called(mock_fisher_yates):
        deck = Deck()
        # Assert FisherYates was called during initialization
        assert mock_fisher_yates.call_count == 1
        # Call shuffle again to verify it's being called
        deck.shuffle()
        assert mock_fisher_yates.call_count == 2
