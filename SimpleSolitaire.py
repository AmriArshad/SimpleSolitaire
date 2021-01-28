import random

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(-1)

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def peeklast(self):
        return self.items[0]

    def printall(self, index):
        if self.size() != 0:
            if index == 0:
                print(str(self.peeklast()), end = "")
                for i in range(1, self.size()):
                    print(" *", end = "")
            else:
                print(str(self.peeklast()), end = "")
                for i in range(1, self.size()):
                    print(" " + str(self.items[i]), end = "")
        
        print("")
            
class Solitaire:
    def __init__(self, ncards):
        self.t = []
        self.__CardNo = len(ncards)
        self.__ColNo = (self.__CardNo // 8) + 3
        self.__ChanceNo = self.__CardNo * 2

        for i in range(self.__ColNo):
            self.t.append(Deque())

        for i in range(self.__CardNo):
            self.t[0].add_front(ncards[i])

    def display(self):
        for i in range(self.__ColNo):
            print(str(i) + ": ", end = "")
            self.t[i].printall(i)

    def move(self, c1, c2):
        if c1 == 0 and c2 == 0:
            last_card = self.t[0].remove_rear()
            self.t[0].add_front(last_card)
        elif c1 == 0 and c2 > 0:
            if self.t[c2].size() != 0:
                N1 = self.t[c1].peeklast()
                N2 = self.t[c2].peek()
                if N2 == N1 + 1:
                    last_card = self.t[0].remove_rear()
                    self.t[c2].add_front(last_card)
            else:
                last_card = self.t[0].remove_rear()
                self.t[c2].add_front(last_card)

        elif c1 > 0 and c2 > 0:
            if self.t[c2].size() != 0:
                N1 = self.t[c1].peeklast()
                N2 = self.t[c2].peek()
                if N2 == N1 + 1:
                    for i in range(self.t[c1].size()):
                        self.t[c2].add_front(self.t[c1].remove_rear())
            else:
                for i in range(self.t[c1].size()):
                    self.t[c2].add_front(self.t[c1].remove_rear())

    def IsComplete(self):
        condition = False
        for i in range(self.__ColNo):
            if self.t[i].size() == self.__CardNo:
                condition = True
                break

        if self.t[0].size() == 0 and condition:
            return True
        return False

    def play(self):
        print("\n*****************************************NEW GAME***************************************")

        for game_iter in range(self.__ChanceNo):
            self.display()

            print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")

            col1 = int(input("Move from row no.:"),10)

            print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")

            col2 = int(input("Move to row no.:"),10)

            if col1 >= 0 and col2 >= 0 and col1 < self.__ColNo and col2 < self.__ColNo:
                self.move(col1, col2)

            if (self.IsComplete() == True):
                print("You Win in", game_iter+1, "steps!")
                break

            else:
                if game_iter+1 == self.__ChanceNo:
                   print("You Lose!")

        print()

def fisher_yates(cards):
    for i in range(len(cards) -1, 0, -1): #iterate from the last card in the deck
        rand_pos = random.randint(0, i) #pick a random position from 0 to i
        temp = cards[i]
        cards[i] = cards[rand_pos]  #swap the card at position i with the random position
        cards[rand_pos] = temp

def overhand(cards):
    shuffle_point = random.randrange(len(cards)//2, len(cards) -1)
    new_cards = cards[shuffle_point:] + cards[0:shuffle_point]
    return new_cards

def riffle(cards):
    shuffle_point = random.randint(len(cards)//2 - 1, len(cards)//2 + 1)
    part1 = cards[:shuffle_point]   #seperate the deck of cards into two parts
    part2 = cards[shuffle_point:]
    
    cards = []

    if len(part1) > len(part2):     #if part 1 is larger than part 2 then we start adding cards from both parts, but starting from part 1
        for i in range(len(part1)):
            try:
                cards.append(part1[i])
                cards.append(part2[i])
            except:
                pass

    else:   #this time starting from part 2
        for i in range(len(part2)):
            try:
                cards.append(part2[i])
                cards.append(part1[i])
            except:
                pass

    return cards

def game_start():
    print("*****************************************Welcome to Solitaire***************************************\n")

    # display menu
    while True:
        try:
            shuffle = int(input("Select your difficulty\n"
            "\n"
            "0. Easy (No shuffle)\n"
            "1. Normal (Overhand shuffle) \n"
            "2. Hard (Riffle shuffle)\n"
            "3. Challenging (Fisher-Yates shuffle)\n"))
            if shuffle < 0 or shuffle > 3:
                print("Please choose a valid difficulty greater than 0 and less than 3\n")
            else:    
                break
        except:
            print("Please choose a valid difficulty by entering it's corresponding number\n")

    while True:
        try:
            total_cards = int(input("How many cards do you want to play with?\n"))
            if total_cards > 14 or total_cards <= 0:
                print("Please enter a number great than 0 and less than 14\n")
            else:
                break
        except:
            print("Please enter a valid number\n")

    cards = [i for i in range(total_cards, 0, -1)]

    if shuffle == 1:
            cards = overhand(cards)
    elif shuffle == 2:
        for i in range(7):
            cards = riffle(cards)
    elif shuffle == 3:
        fisher_yates(cards)

    game = Solitaire(cards)
    game.play()

game_start()