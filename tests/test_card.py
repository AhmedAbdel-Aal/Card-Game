from card_game.card import Card

def test_new_deck_contains_40_cards():
    """
    A new deck should contain 40 cards
    """
    card_1 = Card(1)
    card_2 = Card(2)
    card_1_again = Card(1)
    assert card_1 == card_1_again
    assert card_1 < card_2
    assert card_2 > card_1
