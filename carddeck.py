import random
from playingcard import PlayingCard

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = PlayingCard(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __str__(self):
        return f"CardDeck:{len(self._cards)}"

    def __repr__(self):
        return f"CardDeck()"

if __name__ == "__main__":
    c1 = CardDeck()
    c2 = CardDeck()
    c1.shuffle()
    print(f"{c1.cards = }")
    for _ in range(5):
        c = c1.draw()
        print(f"{c = }")
    print(c1)
    print(f"{c1 = }")
 