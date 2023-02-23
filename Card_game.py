# print("Hello world")
import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print('Number {} of {}'.format(self.value,self.suit))

class deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Hearts","Spades","Diamounds","Clubs"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))

    def show(self):
        for i in self.cards:
            i.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def top(self):
        return self.cards.pop()

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,game):
        self.hand.append(game.top())
        return self

    def showhand(self):
        for pokers in self.hand:
            pokers.show()

    def discard(self):
        return self.hand.pop()
#
var = deck()
var.show()
#
print("\n")

poker = deck()
poker.shuffle()
poker.show()
#
print("\n")

game = deck()
game.shuffle()
#
bob = Player("Gopi")
bob.draw(game).draw(game)
bob.showhand()
bob.discard()
# print("\n")
# bob.showhand()
# pokers  = game.top()
# pokers.show()
