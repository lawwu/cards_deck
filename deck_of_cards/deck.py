# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../01_deck.ipynb 3
from .card import Card

# %% ../01_deck.ipynb 4
class Deck:
    """Represents a deck of cards.
    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        """Initializes the Deck with 52 cards."""
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]

    def __str__(self):
        """Returns a string representation of the deck."""
        return '\n'.join([str(card) in self.cards])
    

    def add_card(self, card:Card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there."""
        self.cards.remove(card)

    def pop_card(self, i=-1 #index of the card to pop; by default, pops the last card.
                ):
        """Removes and returns a card from the deck."""
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, 
                   hand, # destination Hand object 
                   num:int # integer number of cards to move
                  ):
        "Moves the given number of cards from the deck into the Hand."
        for i in range(num): hand.add_card(self.pop_card())