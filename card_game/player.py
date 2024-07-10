from card_game.utils import FisherYates

class Player:
    def __init__(self, name):
        self.name = name
        self.draw_pile = []
        self.discard_pile = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def draw_card(self):
        if len(self.draw_pile) == 0:
            if len(self.discard_pile) == 0:
                return None
            else:
                self.draw_pile = self.discard_pile
                self.discard_pile = []
                self.draw_pile = FisherYates(self.draw_pile)
        return self.draw_pile.pop(0)
    

    def discard_card(self, card):
        self.discard_pile.append(card)
    
    def wins_tied(self, tied_cars):
        self.discard_pile.extend(tied_cars)

    def __str__(self):
        return f'{self.name} ({len(self.draw_pile)} cards) ({len(self.discard_pile)} discard) '