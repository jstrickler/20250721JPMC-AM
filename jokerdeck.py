from playingcard import PlayingCard
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = PlayingCard(f"JOKER {joker_number}", "** JOKER **")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    print(f"{j = }")
    
    j.shuffle()
    print(f"{j.draw() = }")
    print(j)
    