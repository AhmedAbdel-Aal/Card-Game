from card_game.player import Player
from card_game.deck import Deck

class Game:
    """
    A class to represent a game between two players.

    Attributes:
        player_1 (Player): The first player.
        player_2 (Player): The second player.
        tied_cards (list): A list of tied cards during a round.
    """

    def __init__(self, player1_name, player2_name):
        """
        Initializes the game with two players.

        Args:
            player1_name (str): The name of the first player.
            player2_name (str): The name of the second player.
        """
        self.player_1 = Player(player1_name)
        self.player_2 = Player(player2_name)
        self.tied_cards = []
        self.game_log = []
    
    def setup_game(self):
        """
        Sets up the game by creating and shuffling the deck, then distributing the cards to the players.
        """
        deck = Deck()
        for _ in range(20):
            self.player_1.draw_pile.append(deck.draw_card())
            self.player_2.draw_pile.append(deck.draw_card())

    def play_turn(self):
        """
        Plays a turn where each player draws the top card from their draw pile.
        The player with the higher value card wins the round and takes both cards.
        If the cards are of equal value, they are added to the tied_cards pile.

        Returns:
            Player: The winning player if the other player cannot draw a card, otherwise None.
        """
        card_1 = self.player_1.draw_card()
        card_2 = self.player_2.draw_card()
        
        if card_1 is None:
            return self.player_2
        if card_2 is None:
            return self.player_1

        if card_1 > card_2:
            self.player_1.discard_card(card_1)
            self.player_1.discard_card(card_2)
            self.player_1.wins_tied(self.tied_cards)
            #self.player_1.discard_pile.extend([card_1, card_2] + self.tied_cards)
            self.tied_cards = []
            print(f"{self.player_1} wins this round")
            self.game_log.append(f"{self.player_1} wins this round")

        elif card_2 > card_1:
            self.player_2.discard_card(card_1)
            self.player_2.discard_card(card_2)
            self.player_2.wins_tied(self.tied_cards)
            #self.player_2.discard_pile.extend([card_1, card_2] + self.tied_cards)
            self.tied_cards = []
            print(f"{self.player_2} wins this round")
            self.game_log.append(f"{self.player_2} wins this round")

        else:
            self.tied_cards.extend([card_1, card_2])
            print("No winner in this round")
            self.game_log.append("No winner in this round")
