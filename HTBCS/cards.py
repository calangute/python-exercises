'''
@author : C.Manikandan

Chapter : 15 - Sets of Objects

'''

import random

class Card():
    # its not a good idea to modify class variables.
    suitList = ["Clubs","Diamonds","Hearts","Spades"]
    rankList = ["Joker","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def __init__(self, suit=0,rank=2):
        # __init__ intiliases the base values, since this is called after the class is created
        # it is not perfect to call this a "Constructor"!
        self.rank = rank
        self.suit = suit

    def __str__(self):
        #__str__ is used to modify the display string when an object is called.
        return (self.rankList[self.rank] + " of " + self.suitList[self.suit])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank : return 1
        if self.rank < other.rank : return -1
        return 0

class Deck():
    def __init__(self):
        self.cards = []
        for suit in xrange(4):
            for rank in xrange(1,14):
                self.cards.append(Card(suit,rank))

    def __str__(self):
        space = " "
        st = ""
        for i in xrange(len(self.cards)):
            st = st + space*i + str(self.cards[i]) + "\n"
        return st

    def shuffle(self):
        nCards = len(self.cards)
        for i in xrange(nCards):
            r = random.randrange(i,nCards)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def removeCard(self, target):
        if target in self.cards:
            self.cards.remove(cards)
            return true
        else:
            return false

    def popCard(self):
        return self.cards.pop()

    def isEmpty(self):
        return (len(self.cards) == 0)

    def deal(self, hands, nCards =999):
        nHands = len(hands)
        for i in xrange(nCards):
            if self.isEmpty(): break
            card = self.popCard()
            hand = hands[i % nHands]
            hand.addCard(card)

class Hand(Deck):
    def __init__(self,name=""):
        self.name = name
        self.cards=[]

    def addCard(self, newCard):
        self.cards.append(newCard)

    def __str__(self):
        s = "Hand " + "\""+ self.name + "\" "
        if self.isEmpty():
            return s + "is Empty"
        else:
            return s + "contains " + "\n" + Deck.__str__(self)




if __name__=='__main__':
    myDeck = Deck()
    myDeck.shuffle()
    hand = Hand("Mani")
    myDeck.deal([hand],5)
    print hand
