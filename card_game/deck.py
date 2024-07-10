from card_game.card import Card
from card_game.utils import FisherYates

class Deck:
    def __init__(self):
        """
        Initializes a Deck with 40 cards, with values from 1 to 10, each repeated four times.
        """
        self.cards = [Card(value) for value in range(1, 11) for _ in range(4)]
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck using the Fisher-Yates algorithm.
        """
        self.cards = FisherYates(self.cards)
    
    def draw_card(self):
        """
        Draws a card from the deck.

        Returns:
            Card: The drawn card, or None if the deck is empty.
        """
        return self.cards.pop() if self.cards else None

    def __repr__(self):
        return f"Deck({self.cards})"