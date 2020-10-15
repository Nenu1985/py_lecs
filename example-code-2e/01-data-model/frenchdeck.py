import collections
from random import choice
import array
from sys import getsizeof

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def main():
    deck = FrenchDeck()

    print(choice(deck))
    N = 100000
    print('generator', getsizeof((i for i in range(N))))
    print('list', getsizeof([i for i in range(N)])/1000)

    print('array', getsizeof(array.array('i', (i for i in range(N))))/1000)
    print('array I', getsizeof(array.array('I', (i for i in range(N))))/1000)
    print('set', getsizeof(set(i for i in range(N)))/1000)
    

if __name__ == '__main__':
    main()
