from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 j Q K A'.split()

mycards = []

for r in RANKS:
    for s in SUITE:
        mycards.append((s, r))


class Deck:
    def __init__(self):
        print("Createing New Order Deck!")
        self.allcards = mycards

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed:{}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """Return true if player has cards"""
        return len(self.hand.cards) != 0


print("welcome to war!lets begain")

# create a a new deck and split it in half

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# create Computer player

comp = player("computer", Hand(half1))
name = input("what is Your name? ")

user = player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("here are the current standings")

    print(user.name + "has the count: " + str(len(user.hand.cards)))
    print(comp.name + "has the count: " + str(len(comp.hand.cards)))
    print("player a card!")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print("heelo {}".format(RANKS.index(c_card[1])))
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print("game over, Numbe rof rounds:" + str(total_rounds))
print("a war happened" + str(war_count) + " times")
print("Does the Computer still has cards? ")

if comp.still_has_cards():
    print("Computer Won")
if user.still_has_cards():
    print("{} Won".format(user.name))




