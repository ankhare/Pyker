import random
random.seed()
from tkinter import *
from PIL import Image, ImageTk

#generate deck
def generateDeck():
    suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10','Jack', 'Queen','King']

    deck = []

    for suit in suits:
        for rank in ranks:
            card = {'rank': rank,'suit': suit}
            deck += [card]

    return deck
        

def whatKindIsThisHand(hand):

    if isAFlushHand(hand) and isStraightHand(hand):
        return 'straight flush'
    elif isAFlushHand(hand):
        return 'flush'
    elif isStraightHand(hand):
        return 'straight'
    elif isFourOfAKind(hand):
        return 'four of a kind'
    elif isAFullHouse(hand):
        return 'full house'
    elif isThreeOfAKind(hand):
        return 'three of a kind'
    elif isTwoPair(hand):
        return 'two pair'
    elif isOnePair(hand):
        return 'one pair'
    else:
        return 'high card'

def winningHand(hand1, hand2):

    kind1 = whatKindIsThisHand(hand1)
    kind2 = whatKindIsThisHand(hand2)

    hand_rank_value = {'straight flush': 8, 'four of a kind': 7, 'full house': 6, 'flush': 5,\
                  'straight': 4, 'three of a kind': 3, 'two pair': 2, 'one pair': 1, 'high card': 0 }

    rank1 = hand_rank_value[kind1]
    rank2 = hand_rank_value[kind2]

    s = ''

    #determine which hand is higher if both are the same kind
    if rank1 == rank2:

        new_ranks = whichHandIsHigher(hand1, hand2, rank1)
        rank1 = new_ranks[0]
        rank2 = new_ranks[1]

        if rank1 > rank2:
            s = 'Your {} is of higher rank.'.format(kind1)
            
        elif rank2 > rank1:
            s = 'My {} is of higher rank.'.format(kind2)
            
        else:
            s = 'Our hands are of equal rank.'

        print()   

    #determine winner
    if rank1 != rank2:

        if rank1 > rank2:
            result = [1]

        else:
            result = [2]
    else:
        result = [0]

    result += [s]

    return result
           
## if the kind of hand is the same, rank in the following way:
## 0/high card is ranked first by the rank each card from highest to lowest
## 1/one pair is ranked by the rank of its pair and then down to its lowest cards
## 2/two pair is ranked by rank of each of its two pairs and then remaining 1 card
## 3/three of a kind is rank of its three cards and then remaining 2 cards
## 4/straight is only ranked by its highest ranking card
## 5/flush is ranked first by the rank each card from highest to lowest
## 6/full house is ranked by its triplet and then its pair
## 7/four of a kind is ranked by its quadruplet and then remaining card
## 8/straight flush is ranked by its highest card
def whichHandIsHigher(hand1, hand2, kindvalue):
    def rankValueOfCard(card):

            rank_value = {'2':2 , '3': 3, '4': 4, '5':5, '6':6,'7':7,\
                      '8':8, '9':9, '10':10,'Jack':11, 'Queen':12,'King':13, 'Ace': 13}

            rank = card['rank']

            return rank_value[rank]

    hand1.sort(key=rankValueOfCard)
    hand2.sort(key=rankValueOfCard)

    d = {8: [4], 7: [4, 0], 6: [4, 1], 5: [4, 3, 2, 1, 0], 4: [4],\

         3: [4, 1, 0], 2: [4, 2, 0], 1: [4, 2, 1, 0], 0: [4, 3, 2, 1, 0] }

    compare_index = d[kindvalue]

    for n in compare_index:
        card1 = hand1[n]
        card2 = hand2[n]

        highest_rank_value1 = rankValueOfCard(card1)
        highest_rank_value2 = rankValueOfCard(card2)

        if highest_rank_value1 != highest_rank_value2:
            break


    return [highest_rank_value1, highest_rank_value2]


#functions for each hand type:
def isFourOfAKind(hand):
    result = False

    rank_count = {'Ace': 0, '2':0 , '3': 0, '4': 0, '5':0, '6':0,'7':0,\
                  '8':0, '9':0, '10':0,'Jack':0, 'Queen':0,'King':0}

    for card in hand:
        rank_count[card['rank']] += 1
        
    values = rank_count.values()

    if 4 in values:

        result = True
        
    return result

def isAFullHouse(hand):
    result = False

    rank_count = {'Ace': 0, '2':0 , '3': 0, '4': 0, '5':0, '6':0,'7':0,\
                  '8':0, '9':0, '10':0,'Jack':0, 'Queen':0,'King':0}

    for card in hand:
        rank_count[card['rank']] += 1
        
    values = rank_count.values()

    if 3 in values and 2 in values:

        result = True
        
    return result
        

def isAFlushHand(hand):
    result = False

    suit_count = {'Spades': 0, 'Hearts': 0, 'Clubs': 0, 'Diamonds': 0 }

    for card in hand:
        suit_count[card['suit']] += 1

    values = suit_count.values()

    if 5 in values:

        result = True

    return result

def isStraightHand(hand):

    def rankValueOfCard(card):
        
        rank_value = {'2':2 , '3': 3, '4': 4, '5':5, '6':6,'7':7,\
                  '8':8, '9':9, '10':10,'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

        rank = card['rank']
        return rank_value[rank]

    hand.sort(key=rankValueOfCard)
    
    for i in range(1,5):
        prev_card = rankValueOfCard(hand[i-1])

        
        current_card = rankValueOfCard(hand[i])        

        if current_card - prev_card != 1:
            result =  False
            break

        else:
            result = True

    return result
    

def isThreeOfAKind(hand):
    result = False

    rank_count = {'Ace': 0, '2':0 , '3': 0, '4': 0, '5':0, '6':0,'7':0,\
                  '8':0, '9':0, '10':0,'Jack':0, 'Queen':0,'King':0}

    for card in hand:
        rank_count[card['rank']] += 1
        
    values = rank_count.values()

    if 3 in values:

        result = True
        
    return result

def isTwoPair(hand):
    result = False

    rank_count = {'Ace': 0, '2':0 , '3': 0, '4': 0, '5':0, '6':0,'7':0,\
                  '8':0, '9':0, '10':0,'Jack':0, 'Queen':0,'King':0}

    for card in hand:
        rank_count[card['rank']] += 1
        
    values = list(rank_count.values())

    if 2 in values:

        values.remove(2)

        if 2 in values:

            result = True
        
    return result

def isOnePair(hand):
    result = False

    rank_count = {'Ace': 0, '2':0 , '3': 0, '4': 0, '5':0, '6':0,'7':0,\
                  '8':0, '9':0, '10':0,'Jack':0, 'Queen':0,'King':0}

    for card in hand:
        rank_count[card['rank']] += 1
        
    values = list(rank_count.values())

    if 2 in values:

        result = True
        
    return result            
    

if __name__ == '__main__':

    flush = [{'rank': 'Ace', 'suit': 'Hearts' },
             {'rank': '10', 'suit': 'Hearts'},
             {'rank': '5', 'suit': 'Hearts'},
             {'rank': '3', 'suit': 'Hearts'},
             {'rank': 'Queen', 'suit': 'Hearts'}]

    another_flush = [{'rank': 'King', 'suit': 'Hearts' },
                     {'rank': 'Jack', 'suit': 'Hearts'},
                     {'rank': '2', 'suit': 'Hearts'},
                     {'rank': '6', 'suit': 'Hearts'},
                     {'rank': '7', 'suit': 'Hearts'}]

    equivalent_flush = [{'rank': 'King', 'suit': 'Diamonds' },
                     {'rank': 'Jack', 'suit': 'Diamonds'},
                     {'rank': '2', 'suit': 'Diamonds'},
                     {'rank': '6', 'suit': 'Diamonds'},
                     {'rank': '7', 'suit': 'Diamonds'}]


    not_flush = [{'rank': 'Ace', 'suit': 'Hearts' },
                  {'rank': '10', 'suit': 'Spades'},
                  {'rank': '5', 'suit': 'Hearts'},
                  {'rank': '3', 'suit': 'Hearts'},
                  {'rank': 'Queen', 'suit': 'Hearts'}]

    four_of_a_kind = [{'rank': '10', 'suit': 'Spades' },
                      {'rank': '10', 'suit': 'Hearts'},
                      {'rank': '10', 'suit': 'Diamonds'},
                      {'rank': '10', 'suit': 'Clubs'},
                      {'rank': 'Queen', 'suit': 'Hearts'}]

    another_four_of_a_kind = [{'rank': '4', 'suit': 'Spades' },
                              {'rank': '4', 'suit': 'Hearts'},
                              {'rank': '4', 'suit': 'Diamonds'},
                              {'rank': '4', 'suit': 'Clubs'},
                              {'rank': 'Queen', 'suit': 'Diamonds'}]

    not_four_of_a_kind = [{'rank': '9', 'suit': 'Spades' },
                      {'rank': '10', 'suit': 'Hearts'},
                      {'rank': '10', 'suit': 'Diamonds'},
                      {'rank': '10', 'suit': 'Clubs'},
                      {'rank': 'Queen', 'suit': 'Hearts'}]

    full_house = [{'rank': '10', 'suit': 'Spades' },
                  {'rank': '10', 'suit': 'Hearts'},
                  {'rank': '10', 'suit': 'Diamonds'},
                  {'rank': '3', 'suit': 'Hearts'},
                  {'rank': '3', 'suit': 'Clubs'}]

    another_full_house = [{'rank': 'Jack', 'suit': 'Spades' },
                          {'rank': 'Jack', 'suit': 'Hearts'},
                          {'rank': 'Ace', 'suit': 'Diamonds'},
                          {'rank': 'Ace', 'suit': 'Hearts'},
                          {'rank': 'Ace', 'suit': 'Clubs'}]

    not_full_house = [{'rank': 'Jack', 'suit': 'Spades' },
                      {'rank': '10', 'suit': 'Hearts'},
                      {'rank': '10', 'suit': 'Diamonds'},
                      {'rank': '3', 'suit': 'Hearts'},
                      {'rank': '3', 'suit': 'Clubs'}]

    three_of_a_kind = [{'rank': '10', 'suit': 'Spades' },
                      {'rank': '10', 'suit': 'Hearts'},
                      {'rank': '10', 'suit': 'Diamonds'},
                      {'rank': 'Ace', 'suit': 'Clubs'},
                      {'rank': 'Queen', 'suit': 'Hearts'}]

    not_three_of_a_kind = [{'rank': '10', 'suit': 'Spades' },
                           {'rank': '10', 'suit': 'Hearts'},
                           {'rank': '9', 'suit': 'Diamonds'},
                           {'rank': 'Ace', 'suit': 'Clubs'},
                           {'rank': 'Queen', 'suit': 'Hearts'}]

    two_pair = [{'rank': '10', 'suit': 'Spades' },
                {'rank': '10', 'suit': 'Hearts'},
                {'rank': '9', 'suit': 'Diamonds'},
                {'rank': '9', 'suit': 'Clubs'},
                {'rank': 'Queen', 'suit': 'Hearts'}]


    not_two_pair = [{'rank': '10', 'suit': 'Spades' },
                    {'rank': '10', 'suit': 'Hearts'},
                    {'rank': '9', 'suit': 'Diamonds'},
                    {'rank': '8', 'suit': 'Clubs'},
                    {'rank': 'Queen', 'suit': 'Hearts'}]

    one_pair = [{'rank': '10', 'suit': 'Spades' },
                {'rank': '10', 'suit': 'Hearts'},
                {'rank': '3', 'suit': 'Diamonds'},
                {'rank': '9', 'suit': 'Clubs'},
                {'rank': 'Queen', 'suit': 'Hearts'}]

    another_one_pair = [{'rank': '10', 'suit': 'Spades' },
                        {'rank': '10', 'suit': 'Hearts'},
                        {'rank': '4', 'suit': 'Diamonds'},
                        {'rank': '9', 'suit': 'Clubs'},
                        {'rank': 'Queen', 'suit': 'Hearts'}]

    not_one_pair = [{'rank': '10', 'suit': 'Spades' },
                    {'rank': '2', 'suit': 'Hearts'},
                    {'rank': '9', 'suit': 'Diamonds'},
                    {'rank': '4', 'suit': 'Clubs'},
                    {'rank': 'Queen', 'suit': 'Hearts'}]

    straight = [{'rank': '10', 'suit': 'Spades' },
                {'rank': '7', 'suit': 'Hearts'},
                {'rank': '9', 'suit': 'Diamonds'},
                {'rank': '8', 'suit': 'Clubs'},
                {'rank': 'Jack', 'suit': 'Hearts'}]
    
    another_straight = [{'rank': '2', 'suit': 'Spades' },
                        {'rank': '3', 'suit': 'Hearts'},
                        {'rank': '4', 'suit': 'Diamonds'},
                        {'rank': '5', 'suit': 'Clubs'},
                        {'rank': '6', 'suit': 'Hearts'}]

    not_straight = [{'rank': '10', 'suit': 'Spades' },
                    {'rank': '7', 'suit': 'Hearts'},
                    {'rank': '9', 'suit': 'Diamonds'},
                    {'rank': '8', 'suit': 'Clubs'},
                    {'rank': 'Queen', 'suit': 'Hearts'}]

    straight_flush = [{'rank': 'Jack', 'suit': 'Hearts' },
                      {'rank': '10', 'suit': 'Hearts'},
                      {'rank': '9', 'suit': 'Hearts'},
                      {'rank': '8', 'suit': 'Hearts'},
                      {'rank': '7', 'suit': 'Hearts'}]

    another_straight_flush = [{'rank': 'Ace', 'suit': 'Spades' },
                              {'rank': 'King', 'suit': 'Spades'},
                              {'rank': 'Queen', 'suit': 'Spades'},
                              {'rank': 'Jack', 'suit': 'Spades'},
                              {'rank': '10', 'suit': 'Spades'}]

    not_straight_flush = [{'rank': 'Jack', 'suit': 'Hearts' },
                          {'rank': '10', 'suit': 'Hearts'},
                          {'rank': '9', 'suit': 'Spades'},
                          {'rank': '8', 'suit': 'Hearts'},
                          {'rank': '7', 'suit': 'Hearts'}]

    high_card =    [{'rank': '2', 'suit': 'Spades' },
                    {'rank': '7', 'suit': 'Hearts'},
                    {'rank': '9', 'suit': 'Diamonds'},
                    {'rank': '8', 'suit': 'Clubs'},
                    {'rank': 'King', 'suit': 'Hearts'}]

    another_high_card = [{'rank': '5', 'suit': 'Clubs' },
                    {'rank': '7', 'suit': 'Diamonds'},
                    {'rank': '9', 'suit': 'Hearts'},
                    {'rank': '8', 'suit': 'Spades'},
                    {'rank': 'King', 'suit': 'Hearts'}]

    not_high_card = [ {'rank': '2', 'suit': 'Spades' },
                      {'rank': '2', 'suit': 'Hearts'},
                      {'rank': '9', 'suit': 'Diamonds'},
                      {'rank': '8', 'suit': 'Clubs'},
                      {'rank': 'Queen', 'suit': 'Hearts'}]

    test_cases = [[straight_flush, not_straight_flush, 'straight flush'],

                  [full_house, not_full_house, 'full house'],

                  [four_of_a_kind, not_four_of_a_kind, 'four of a kind'],

                  [flush, not_flush, 'flush'],

                  [straight, not_straight, 'straight'],
                  
                  [three_of_a_kind, not_three_of_a_kind, 'three of a kind'],
                  
                  [two_pair, not_two_pair, 'two pair'],
                  
                  [one_pair, not_one_pair, 'one pair'],
                  
                  [high_card, not_high_card, 'high card']]

    print('testing cases in list test_cases:')
    print()

#test cases for each kind function 
    for case in test_cases:

        positive_hand = case[0]
        negative_hand = case[1]
        expected_result = case[2]

        result = whatKindIsThisHand(positive_hand)
        
        if result == expected_result:
            print('pass')

        else:
             print('{} valid test case FAIL. returned: {}'.format(expected_result, whatKindIsThisHand(positive_hand)))

        result = whatKindIsThisHand(negative_hand)

        if result != expected_result:
            print('pass')

        else:
            print('{} invalid test case FAIL. returned: {}'.format(expected_result, whatKindIsThisHand(negative_hand)))


#test winnningHand function
    print()
    print('testing winning hand function:')
    
    users = [flush, four_of_a_kind, straight, high_card, \
             full_house, high_card, another_straight_flush,\
             another_straight, another_full_house, another_one_pair, another_flush, another_flush, four_of_a_kind]

    computers = [straight_flush, two_pair, not_straight, \
                 one_pair, not_high_card, another_high_card,\
                 straight_flush, straight, full_house, one_pair, flush, equivalent_flush, another_four_of_a_kind]

    expected_results = [2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 0, 1]

    for i in range(len(users)):
        user = users[i]
        computer = computers[i]
        expected_result = expected_results[i]

        result = (winningHand(user, computer))[0]

        if result == expected_result:
            print('pass')
        else:
            print('fail, expected: {}, returned: {}'.format(expected_result, result ))     
