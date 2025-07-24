class PlayingCard:  # inherits from 'object'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):  # getter property (AKA public variable)
        return self._rank
    
    @rank.setter
    def rank(self, value):  # setter property
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a string")

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        self._suit = value

    def __str__(self):
        return f"{self.rank}/{self.suit}"

    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = PlayingCard('A', 'Hearts')
    c2 = PlayingCard('8', 'Diamonds')
    print(f"{c1 = }")
    print(f"{c2 = }")
    print(f"{c1.rank = }")
    print(f"{c2.suit = }")
    print(c1)  # str(c1)
    print(c2)
    print(f"{c1 = }")   # repr(c1)
    print(f"{c2 = }")
