from typing import Type
import random
from collections import Counter
import math

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print(f'Invalid card: {suit} {rank}')

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return VALUES[self.rank]


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = "Hand contains "
        for i in range(len(self.cards)):
            ans += str(self.cards[i]) + " "
        return ans
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        value = 0
        aces = False
        for c in self.cards:
            rank = c.get_rank()
            v = VALUES[rank]
            if rank == 'A': aces = True
            value += v
        if aces and value < 12: value += 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck

    def __str__(self):
        ans = "The deck: "
        for c in self.deck:
            ans += str(c) + " "
        return ans
        # return a string representing the deck

def run_game(player):

    theDeck = Deck()
    theDeck.shuffle()
    #print theDeck
    playerhand = Hand()
    househand = Hand()
    playerhand.add_card(theDeck.deal_card())
    playerhand.add_card(theDeck.deal_card())
    househand.add_card(theDeck.deal_card())
    househand.add_card(theDeck.deal_card())
    
    while playerhand.get_value() < 21:
        hit =  player.hitme(playerhand, househand.cards[0])
        
        if hit == False:

            break
        else:
            playerhand.add_card(theDeck.deal_card())

    if playerhand.get_value() > 21:
        return 0
    
    val = househand.get_value()
    while(val < 17):
        househand.add_card(theDeck.deal_card())
        val = househand.get_value()  
        # print "House:", househand, "Value:", val
    if (val > 21):
    # print "House is busted!"
        return 1

    if (val == playerhand.get_value()):
        # outcome = "House wins ties!"
        return 0
    elif (val > playerhand.get_value()):
        # outcome = "House wins!"
        return 0
    else:
        # outcome = "Player wins!"
        return 1
    

tracking = True
scenarios = []
scenario_outcomes = Counter()
scenario_counter = Counter()

# define player class
class Player:

    def __init__(self):
        #format: player hand value, dealer card value, soft total = True else False : hit = true, stay = false
        self.matrix = {(2, 1, True) : True ,
                          (2, 2, True) : True ,
                          (2, 3, True) : True ,
                          (2, 4, True) : True ,
                          (2, 5, True) : True ,
                          (2, 6, True) : True ,
                          (2, 7, True) : True ,
                          (2, 8, True) : True ,
                          (2, 9, True) : True ,
                          (2, 10, True) : True ,
                          (3, 1, True) : True ,
                          (3, 2, True) : True ,
                          (3, 3, True) : True ,
                          (3, 4, True) : True ,
                          (3, 5, True) : True ,
                          (3, 6, True) : True ,
                          (3, 7, True) : True ,
                          (3, 8, True) : True ,
                          (3, 9, True) : True ,
                          (3, 10, True) : True ,
                          (4, 1, False) : True ,
                          (4, 1, True) : True ,
                          (4, 2, False) : False ,
                          (4, 2, True) : True ,
                          (4, 3, False) : True ,
                          (4, 3, True) : True ,
                          (4, 4, False) : True ,
                          (4, 4, True) : True ,
                          (4, 5, False) : True ,
                          (4, 5, True) : True ,
                          (4, 6, False) : True ,
                          (4, 6, True) : True ,
                          (4, 7, False) : True ,
                          (4, 7, True) : True ,
                          (4, 8, False) : True ,
                          (4, 8, True) : True ,
                          (4, 9, False) : True ,
                          (4, 9, True) : True ,
                          (4, 10, False) : True ,
                          (4, 10, True) : True ,
                          (5, 1, False) : True ,
                          (5, 1, True) : True ,
                          (5, 2, False) : True ,
                          (5, 2, True) : True ,
                          (5, 3, False) : True ,
                          (5, 3, True) : True ,
                          (5, 4, False) : True ,
                          (5, 4, True) : True ,
                          (5, 5, False) : True ,
                          (5, 5, True) : True ,
                          (5, 6, False) : True ,
                          (5, 6, True) : True ,
                          (5, 7, False) : True ,
                          (5, 7, True) : True ,
                          (5, 8, False) : True ,
                          (5, 8, True) : True ,
                          (5, 9, False) : True ,
                          (5, 9, True) : True ,
                          (5, 10, False) : True ,
                          (5, 10, True) : True ,
                          (6, 1, False) : True ,
                          (6, 1, True) : True ,
                          (6, 2, False) : True ,
                          (6, 2, True) : True ,
                          (6, 3, False) : True ,
                          (6, 3, True) : True ,
                          (6, 4, False) : True ,
                          (6, 4, True) : True ,
                          (6, 5, False) : True ,
                          (6, 5, True) : True ,
                          (6, 6, False) : True ,
                          (6, 6, True) : True ,
                          (6, 7, False) : True ,
                          (6, 7, True) : True ,
                          (6, 8, False) : True ,
                          (6, 8, True) : True ,
                          (6, 9, False) : True ,
                          (6, 9, True) : True ,
                          (6, 10, False) : True ,
                          (6, 10, True) : True ,
                          (7, 1, False) : True ,
                          (7, 1, True) : True ,
                          (7, 2, False) : True ,
                          (7, 2, True) : True ,
                          (7, 3, False) : True ,
                          (7, 3, True) : True ,
                          (7, 4, False) : True ,
                          (7, 4, True) : True ,
                          (7, 5, False) : True ,
                          (7, 5, True) : True ,
                          (7, 6, False) : True ,
                          (7, 6, True) : True ,
                          (7, 7, False) : True ,
                          (7, 7, True) : True ,
                          (7, 8, False) : True ,
                          (7, 8, True) : True ,
                          (7, 9, False) : True ,
                          (7, 9, True) : True ,
                          (7, 10, False) : True ,
                          (7, 10, True) : True ,
                          (8, 1, False) : True ,
                          (8, 1, True) : False ,
                          (8, 2, False) : True ,
                          (8, 2, True) : False ,
                          (8, 3, False) : True ,
                          (8, 3, True) : False ,
                          (8, 4, False) : True ,
                          (8, 4, True) : False ,
                          (8, 5, False) : True ,
                          (8, 5, True) : False ,
                          (8, 6, False) : True ,
                          (8, 6, True) : False ,
                          (8, 7, False) : True ,
                          (8, 7, True) : False ,
                          (8, 8, False) : True ,
                          (8, 8, True) : True ,
                          (8, 9, False) : True ,
                          (8, 9, True) : True ,
                          (8, 10, False) : True ,
                          (8, 10, True) : True ,
                          (9, 1, False) : True ,
                          (9, 1, True) : False ,
                          (9, 2, False) : True ,
                          (9, 2, True) : False ,
                          (9, 3, False) : True ,
                          (9, 3, True) : False ,
                          (9, 4, False) : True ,
                          (9, 4, True) : False ,
                          (9, 5, False) : True ,
                          (9, 5, True) : False ,
                          (9, 6, False) : True ,
                          (9, 6, True) : False ,
                          (9, 7, False) : True ,
                          (9, 7, True) : False ,
                          (9, 8, False) : True ,
                          (9, 8, True) : False ,
                          (9, 9, False) : True ,
                          (9, 9, True) : False ,
                          (9, 10, False) : True ,
                          (9, 10, True) : False ,
                          (10, 1, False) : True ,
                          (10, 1, True) : False ,
                          (10, 2, False) : True ,
                          (10, 2, True) : False ,
                          (10, 3, False) : True ,
                          (10, 3, True) : False ,
                          (10, 4, False) : True ,
                          (10, 4, True) : False ,
                          (10, 5, False) : True ,
                          (10, 5, True) : False ,
                          (10, 6, False) : True ,
                          (10, 6, True) : False ,
                          (10, 7, False) : True ,
                          (10, 7, True) : False ,
                          (10, 8, False) : True ,
                          (10, 8, True) : False ,
                          (10, 9, False) : True ,
                          (10, 9, True) : False ,
                          (10, 10, False) : True ,
                          (10, 10, True) : False ,
                          (11, 1, False) : True ,
                          (11, 2, False) : True ,
                          (11, 3, False) : True ,
                          (11, 4, False) : True ,
                          (11, 5, False) : True ,
                          (11, 6, False) : True ,
                          (11, 7, False) : True ,
                          (11, 8, False) : True ,
                          (11, 9, False) : True ,
                          (11, 10, False) : True ,
                          (12, 1, False) : True ,
                          (12, 1, True) : True ,
                          (12, 2, False) : False ,
                          (12, 2, True) : False ,
                          (12, 3, False) : False ,
                          (12, 3, True) : False ,
                          (12, 4, False) : False ,
                          (12, 4, True) : False ,
                          (12, 5, False) : False ,
                          (12, 5, True) : False ,
                          (12, 6, False) : False ,
                          (12, 6, True) : False ,
                          (12, 7, False) : True ,
                          (12, 7, True) : True ,
                          (12, 8, False) : True ,
                          (12, 8, True) : True ,
                          (12, 9, False) : True ,
                          (12, 9, True) : True ,
                          (12, 10, False) : True ,
                          (12, 10, True) : True ,
                          (13, 1, False) : True ,
                          (13, 1, True) : True ,
                          (13, 2, False) : False ,
                          (13, 2, True) : False ,
                          (13, 3, False) : False ,
                          (13, 3, True) : False ,
                          (13, 4, False) : False ,
                          (13, 4, True) : False ,
                          (13, 5, False) : False ,
                          (13, 5, True) : False ,
                          (13, 6, False) : False ,
                          (13, 6, True) : False ,
                          (13, 7, False) : True ,
                          (13, 7, True) : True ,
                          (13, 8, False) : True ,
                          (13, 8, True) : True ,
                          (13, 9, False) : True ,
                          (13, 9, True) : True ,
                          (13, 10, False) : True ,
                          (13, 10, True) : True ,
                          (14, 1, False) : True ,
                          (14, 1, True) : True ,
                          (14, 2, False) : False ,
                          (14, 2, True) : False ,
                          (14, 3, False) : False ,
                          (14, 3, True) : False ,
                          (14, 4, False) : False ,
                          (14, 4, True) : False ,
                          (14, 5, False) : False ,
                          (14, 5, True) : False ,
                          (14, 6, False) : False ,
                          (14, 6, True) : False ,
                          (14, 7, False) : True ,
                          (14, 7, True) : True ,
                          (14, 8, False) : True ,
                          (14, 8, True) : True ,
                          (14, 9, False) : True ,
                          (14, 9, True) : True ,
                          (14, 10, False) : True ,
                          (14, 10, True) : True ,
                          (15, 1, False) : True ,
                          (15, 1, True) : True ,
                          (15, 2, False) : False ,
                          (15, 2, True) : False ,
                          (15, 3, False) : False ,
                          (15, 3, True) : False ,
                          (15, 4, False) : False ,
                          (15, 4, True) : False ,
                          (15, 5, False) : False ,
                          (15, 5, True) : False ,
                          (15, 6, False) : False ,
                          (15, 6, True) : False ,
                          (15, 7, False) : True ,
                          (15, 7, True) : True ,
                          (15, 8, False) : True ,
                          (15, 8, True) : True ,
                          (15, 9, False) : False ,
                          (15, 9, True) : True ,
                          (15, 10, False) : False ,
                          (15, 10, True) : False ,
                          (16, 1, False) : True ,
                          (16, 1, True) : True ,
                          (16, 2, False) : False ,
                          (16, 2, True) : False ,
                          (16, 3, False) : False ,
                          (16, 3, True) : False ,
                          (16, 4, False) : False ,
                          (16, 4, True) : False ,
                          (16, 5, False) : False ,
                          (16, 5, True) : False ,
                          (16, 6, False) : False ,
                          (16, 6, True) : False ,
                          (16, 7, False) : True ,
                          (16, 7, True) : False ,
                          (16, 8, False) : True ,
                          (16, 8, True) : False ,
                          (16, 9, False) : False ,
                          (16, 9, True) : False ,
                          (16, 10, False) : False ,
                          (16, 10, True) : False ,
                          (17, 1, False) : True ,
                          (17, 1, True) : True ,
                          (17, 2, False) : False ,
                          (17, 2, True) : False ,
                          (17, 3, False) : False ,
                          (17, 3, True) : False ,
                          (17, 4, False) : False ,
                          (17, 4, True) : False ,
                          (17, 5, False) : False ,
                          (17, 5, True) : False ,
                          (17, 6, False) : False ,
                          (17, 6, True) : False ,
                          (17, 7, False) : False ,
                          (17, 7, True) : False ,
                          (17, 8, False) : False ,
                          (17, 8, True) : False ,
                          (17, 9, False) : False ,
                          (17, 9, True) : False ,
                          (17, 10, False) : False ,
                          (17, 10, True) : False ,
                          (18, 1, False) : False ,
                          (18, 1, True) : False ,
                          (18, 2, False) : False ,
                          (18, 2, True) : False ,
                          (18, 3, False) : False ,
                          (18, 3, True) : False ,
                          (18, 4, False) : False ,
                          (18, 4, True) : False ,
                          (18, 5, False) : False ,
                          (18, 5, True) : False ,
                          (18, 6, False) : False ,
                          (18, 6, True) : False ,
                          (18, 7, False) : False ,
                          (18, 7, True) : False ,
                          (18, 8, False) : False ,
                          (18, 8, True) : False ,
                          (18, 9, False) : False ,
                          (18, 9, True) : False ,
                          (18, 10, False) : False ,
                          (18, 10, True) : False ,
                          (19, 1, False) : False ,
                          (19, 1, True) : False ,
                          (19, 2, False) : False ,
                          (19, 2, True) : False ,
                          (19, 3, False) : False ,
                          (19, 3, True) : False ,
                          (19, 4, False) : False ,
                          (19, 4, True) : False ,
                          (19, 5, False) : False ,
                          (19, 5, True) : False ,
                          (19, 6, False) : False ,
                          (19, 6, True) : False ,
                          (19, 7, False) : False ,
                          (19, 7, True) : False ,
                          (19, 8, False) : False ,
                          (19, 8, True) : False ,
                          (19, 9, False) : False ,
                          (19, 9, True) : False ,
                          (19, 10, False) : False ,
                          (19, 10, True) : False ,
                          (20, 1, False) : False ,
                          (20, 1, True) : False ,
                          (20, 2, False) : False ,
                          (20, 2, True) : False ,
                          (20, 3, False) : False ,
                          (20, 3, True) : False ,
                          (20, 4, False) : False ,
                          (20, 4, True) : False ,
                          (20, 5, False) : False ,
                          (20, 5, True) : False ,
                          (20, 6, False) : False ,
                          (20, 6, True) : False ,
                          (20, 7, False) : False ,
                          (20, 7, True) : False ,
                          (20, 8, False) : False ,
                          (20, 8, True) : False ,
                          (20, 9, False) : False ,
                          (20, 9, True) : False ,
                          (20, 10, False) : False ,
                          (20, 10, True) : False} # to define


    def sim(self, trials: int) -> None:
        if trials == 0:
            print("ERROR: cannot run 0 trials")
            return 0

        # run random trials and update the matrix
        global tracking, scenarios, scenario_outcomes, scenario_counter
        tracking = True
        scenario_outcomes = Counter()
        scenario_counter = Counter()

        wins = 0
        for i in range(trials):
            outcome = run_game(self)
            wins += outcome
            
            for scenario in scenarios:
                scenario_counter[scenario] += 1
                scenario_outcomes[scenario] += outcome
            scenarios = []
        
        sorted_keys = list(scenario_counter.keys()).copy()
        sorted_keys.sort()
        for key in sorted_keys:
            # print("scenario:", key, "occurences:", scenario_counter[key], "wins:", scenario_outcomes[key])
            if key[3] == True:
                #scenario where we hit
                stand_key = (key[0], key[1], key[2], False)

                # check if scenario_counter[key] == 0 or scenario_counter[stand_key] == 0? :
                try: 
                    if scenario_outcomes[key] / scenario_counter[key] > scenario_outcomes[stand_key] / scenario_counter[stand_key]:
                        self.matrix[(key[0], key[1], key[2])] = True
                        # print("                         ", (key[0], key[1], key[2]), ":", "True", ",")
                    else:
                        self.matrix[(key[0], key[1], key[2])] = False
                        # print("                         ", (key[0], key[1], key[2]), ":", "False", ",")
                except:
                    pass
        # print("len(sorted_keys):",len(sorted_keys))

    def hitme(self, playerhand: Type[Hand], dealerfacecard: Type[Card]) -> bool:
        # use the matrix to decide whether to hit
        if playerhand is None or dealerfacecard is None:
            # print("ERROR: No hand in play")
            return False
        if playerhand.get_value() == 21: return False

        player_values = []
        soft = False
        for card in playerhand.cards:
            rank = VALUES[card.get_rank()]
            if rank == 1:
                soft = True
            player_values.append(rank)

        if tracking:
            hit_key = (sum(player_values), VALUES[dealerfacecard.get_rank()], soft, True)
            stand_key = (sum(player_values), VALUES[dealerfacecard.get_rank()], soft, False)
            if scenario_counter[hit_key] <= 100 or scenario_counter[stand_key] <= 100:
                choice = random.choice((True, False))
            else:
                #use MCTS UCB formula to exploit vs explore
                value_hit = scenario_outcomes[hit_key] / scenario_counter[hit_key] + 1.0 * math.sqrt(2 * math.log(scenario_counter[hit_key] + scenario_counter[stand_key]) / scenario_counter[hit_key])
                value_stand = scenario_outcomes[stand_key] / scenario_counter[stand_key] + 1.0 * math.sqrt(2 * math.log(scenario_counter[hit_key] + scenario_counter[stand_key]) / scenario_counter[stand_key])
                if value_hit > value_stand:
                    choice = True
                else:
                    choice = False
            # player_values.sort()
            scenarios.append((sum(player_values), VALUES[dealerfacecard.get_rank()], soft, choice))
            # scenarios.append((tuple(player_values), VALUES[dealerfacecard.get_rank()], choice))
        else:
            choice = self.matrix[(sum(player_values), VALUES[dealerfacecard.get_rank()], soft)]

        return choice
        # if playerhand.get_value() > 16: 
        #     return False
        # else:
        #     return True
        

    def play(self, trials: int) -> float:
        # play out trials with the learned matrix
        global tracking 
        tracking = False

        wins = 0
        for i in range(trials):
            outcome = run_game(self)
            wins += outcome

        if trials == 0:
            # print("ERROR: cannot run 0 trials")
            return 0.0

        # print("winning percentage = ", (float(wins)/float(trials)) * 100, "%")
        return (float(wins)/float(trials))
            

# p = Player()
# p.sim(5_000_000)
# print(f"winning percentage = {p.play(100_000)}%") 


