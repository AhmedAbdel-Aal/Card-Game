class Card:
    """
    A class representing a single card in the deck.

    Attributes:
        value (int): The value of the card, ranging from 1 to 10.
    """
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return str(self.value)