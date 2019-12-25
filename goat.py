#!/usr/bin/python3

import random 
import statistics

# simulate game
turns=1000000
print("running ", turns)
player1_static_wins=0
player2_dyn_wins=0
for i in range(turns):
    goat = random.randint(1,3)
    ##print("goat on ", goat)
    play1_bet = play2_bet = random.randint(1,3)
    # same bet for both players (this helps simplifying some code ahead...)
    #play2_bet = random.randint(1,3)
    ##print("play1 ", play1_bet)
    ##print("play2 ", play2_bet)

    # if WIN_IMMEDIATE, calculate and finish already the game
    # not doing this...

    #time to open door with no goat
    doors = list(range(1,4))
    doors.remove(goat)
    if goat != play2_bet:       # just avoid duplication of .remove() for same element
        doors.remove(play2_bet) # same bet as play1
    no_goat = doors[random.randint(0,len(doors)-1)]

    #player1 will keep its door
    #player2 will change
    p2doors = list(range(1,4))
    p2doors.remove(play2_bet)
    p2doors.remove(no_goat) 
    play2_bet = p2doors[0]  # only last option
    if play1_bet == goat:
        player1_static_wins+=1
    if play2_bet == goat:
        player2_dyn_wins+=1
        

# if goat cannot appear on first round, chance is 1/3 and 2/3=66.6%
# if goat can appear (and win immediately), then chance is 1/3 and (4/3+1)/3=77.7% (see WIN_IMMEDIATE option)

print("player1 = ", player1_static_wins, " -> ",player1_static_wins/turns, '%')
print("player2 = ", player2_dyn_wins, " -> ",player2_dyn_wins/turns, '%')
