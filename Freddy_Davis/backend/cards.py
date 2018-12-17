from random import shuffle
lst_suite = 'H D S C'.split()
lst_ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.lst_allcards =[(s,r) for s in lst_suite for r in lst_ranks]

    def shuffle(self):
        shuffle(lst_allcards)

    def split_in_half(self):
        return(self.lst_allcards[:26],self.lst_allcards[26:])

class Hand:
     def __init__(self,cards):
         self.cards =cards

     def __str__(self):
         return "contains {} cards".format(len(self.cards))

     def add(self,added_cards):
        self.cards.extend(added_cards)

     def remove_card(self):
         return self.cards.pop()


class Player:

    def __init__(self,name,hand):
         self.name =name
         self.hand =hand

    def play_card(self):
        drawn_card=self.hand.remove_card()
        print("{} has placed : {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
