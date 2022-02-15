from random import *
import random
from math import *
import math

# Chapter 9 Exercises

"""

# Exercise 9.1

# Revise the racquetball simulation so that it computes the results for best
# of n game matches. First service alternates, so player A serves first in the
# odd games of the match, and player B serves first in the even games.

def racquetball():
    printlntro()
    probA, probB, n = getlnputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printlntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. First serve alternates.")

def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    
    winsA = winsB = 0
    
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i+1)
    
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB, gameRound):
    
    # Simulates a single game of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    scoreA = 0
    scoreB = 0
    
    if gameRound % 2 == 1:
        serving = "A"
    else:
        serving = "B"
    
    scoreA = 0
    scoreB = 0
    
    while not gameOver(scoreA, scoreB):
        if serving == "A" :
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))

racquetball()


# Exercise 9.3

# Design and implement a simulation of the game of volleyball. Normal
# volleyball is played like racquetball in that a team can only score points
# when it is serving. Games are played to 15, but must be won by at least
# two points.

def volleyball():
    printVolleylntro()
    probA, probB, n = getVolleylnputs()
    winsA, winsB = simNVolleyGames(n, probA, probB)
    printVolleySummary(winsA, winsB)

def printVolleylntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B". The ability of each team to score is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. First serve alternates.")

def getVolleylnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. team A wins a serve? "))
    b = float(input("What is the prob. team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNVolleyGames(n, probA, probB):
    
    # Simulates n games of volleyball between teams whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    
    winsA = winsB = 0
    
    for i in range(n):
        scoreA, scoreB = simOneVolleyGame(probA, probB, i+1)
    
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneVolleyGame(probA, probB, gameRound):
    
    # Simulates a single game of volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    scoreA = 0
    scoreB = 0
    
    if gameRound % 2 == 1:
        serving = "A"
    else:
        serving = "B"
    
    scoreA = 0
    scoreB = 0
    
    while not gameOver(scoreA, scoreB):
        if serving == "A" :
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    if (a >= 15 and a - 2 >= b) or (b >= 15 and b - 2 >= a):
        return True
    return False

def printVolleySummary(winsA, winsB):
    # Prints a summary of wins for each team.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for team A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Wins for team B: {0} ({1: 0.1%})".format(winsB, winsB/n))

# Exercise 9.4

# Most sanctioned volleyball is now played using rally scoring. In this system,
# the team that wins a rally is awarded a point, even if they were not
# the serving team. Games are played to a score of 25. Design and implement
# a simulation of volleyball using rally scoring.

def volleyballRallyVersion():
    print("This is based on the rally version of volleyball.")
    printVolleylntro()
    probA, probB, n = getVolleylnputs()
    winsA, winsB = simNVolleyRallyGames(n, probA, probB)
    printVolleySummary(winsA, winsB)

def simNVolleyRallyGames(n, probA, probB):
    
    # Simulates n games of volleyball between teams whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    
    winsA = winsB = 0
    
    for i in range(n):
        scoreA, scoreB = simOneVolleyGameRally(probA, probB, i+1)
    
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB    

def simOneVolleyGameRally(probA, probB, gameRound):
    
    # Simulates a single game of volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B

    scoreA = 0
    scoreB = 0
    
    if gameRound % 2 == 1:
        serving = "A"
    else:
        serving = "B"
    
    scoreA = 0
    scoreB = 0
    
    while not gameOverRally(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
    return scoreA, scoreB

def gameOverRally(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    if (a >= 25 and a - 2 >= b) or (b >= 25 and b - 2 >= a):
        return True
    return False

print()

# Exercise 9.5

# Design and implement a system that compares regular volleyball games
# to those using rally scoring. Your program should be able to investigate
# whether rally scoring magnifies, reduces, or has no effect on the relative
# advantage enjoyed by the better team.

print("Test 100 games with uneven chances of scoring: 70% for A, 50% for B")
volleyball()
volleyballRallyVersion()
print("Test 100 games with slightly uneven chances of scoring: 80% for A," +
      " 72% for B")
volleyball()
volleyballRallyVersion()
print("Test 100 games of equivalent chances of scoring: 65% for A, 65% for B")
volleyball()
volleyballRallyVersion()

# Answer: Rally scoring makes games far less lopsided.



# Exercise 9.7

# Craps is a dice game played at many casinos. A player rolls a pair of normal
# six-sided dice. If the initial roll is 2, 3, or 12, the player loses. If the
# roll is 7 or 11, the player wins. Any other initial roll causes the player
# to "roll for point." That is, the player keeps rolling the dice until
# either rolling a 7 or re-rolling the value of the initial roll. If the
# player re-rolls the initial value before rolling a 7, it's a win.
# Rolling a 7 first is a loss.

# Write a program to simulate multiple games of craps and estimate the
# probability that the player wins. For example, if the player wins 249 out of
# 500 games, then the estimated probability of winning is 249/500 = 0.498.

def craps():
    printIntro()
    simulateGame()

def printIntro():
    print("This program simulates a certain number of games of craps.")


def simulateGame():
    
    n = int(input("How many games of craps would you like to simulate? "))

    wins = losses = 0
    
    for i in range(n):
        if not rollDice():
            losses += 1
        else:
            wins += 1
            
    printSummary(wins, losses, n)


def rollDice():
    
    # Roll 2 dice
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    sum = dice1 + dice2

    if sum == 2 or sum == 3 or sum == 12:
        return False
    if sum == 7 or sum == 11:
        return True

    initial_roll = sum
    sum = 0

    while (sum != 7 and sum != initial_roll):
        dice1 = randrange(1, 7)
        dice2 = randrange(1, 7)
        sum = dice1 + dice2

        if sum == 7:
            return False
        if sum == initial_roll:
            return True
        
def printSummary(wins, losses, n):
    print(f"Total wins: {wins}")
    print(f"Total losses: {losses}")
    print(f"Your win rate is {wins/n}")

craps()


# Exercise 9.8

# Blackjack (twenty-one) is a casino game played with cards. The goal of the
# game is to draw cards that total as close to 21 points as possible without
# going over. All face cards count as 10 points, aces count as 1 or 11, and all
# other cards count their numeric value.

# The game is played against a dealer. The player tries to get closer to
# 21 (without going over) than the dealer. If the dealer busts (goes over
# 21), the player automatically wins (provided the player had not already
# busted). The dealer must always take cards according to a fixed set of
# rules. The dealer takes cards until he or she achieves a total of at least
# 17. If the dealer's hand contains an ace, it will be counted as 11 when
# that results in a total between 17 and 21 inclusive; otherwise, the ace is
# counted as 1.

# Write a program that simulates multiple games of blackjack and estimates
# the probability that the dealer will bust. Hints: Treat the deck of
# cards as infinite (casinos use a "shoe" containing many decks). You do not
# need to keep track of the cards in the hand, just the total so far (treating
# an ace as 1) and a bool variable hasAce that tells whether or not the
# hand contains an ace. A hand containing an ace should have 10 points
# added to the total exactly when doing so would produce a stopping total
# (something between 17 and 21 inclusive).

def blackjack():
    printIntro()
    simulateBlackjackGames()

def printIntro():

    print()
    print("This is a game of blackjack.")
    print()

def simulateBlackjackGames():

    n = getNumberOfGames()
        
    wins = losses = draws = 0
    
    for i in range(n):
        print()
        player_total = givePlayerCards()
        print()
        dealer_total = giveDealerCards()

        if player_total > 21:
            print("Sorry you busted! You lose!")
            losses += 1
        elif dealer_total > 21:
            print("Congratulations! The dealer busted so you win!")
            wins += 1
        elif player_total > dealer_total:
            print("Congratulations! Your total is greater than the dealer's!")
            print("You win this round.")
            wins += 1
        elif dealer_total > player_total:
            print("Unfortunately the dealer's total is greater than yours.")
            print("You lose this round.")
            losses += 1
        else:
            print("Both you and the dealer had the same total - a draw.")
            draws += 1

    printSummary(wins, losses, draws, n)


def getNumberOfGames():

    n = 0
    
    while True:
        try:
            n = int(input("How many games of Blackjack do you want to play? "))
            if n <= 0:
                raise Exception
        except ValueError:
            print("Please enter a number.")
            continue
        except Exception:
            print("Please enter a positive integer.")
            continue
        break
    
    return n


def givePlayerCards():

    sum = 0
    hasAce = False
    response = "y"
    
    while True:
        
        response = input(f"Do you want to draw a card? Your " +
                         f"total is currently {sum}. Type \"y\" or \"n\": ")

        if response == "n" or response == "N":
            return sum
            
        card = randrange(1, 14)

        if card == 11:
            print("You just drew a Jack.")
        if card == 12:
            print("You just drew a Queen.")
        if card == 13:
            print("You just drew a King.")
        
        if card == 1:
            print("You just drew an Ace.")
            hasAce = True
            if sum + 11 >= 17 and sum + 11 <= 21:
                sum += 11
            else:
                sum += 1
        elif card >= 2 and card <= 10:
            print(f"You just drew a {card}.")
            if hasAce == True and sum + card + 10 >= 17 and sum + card + 10 <= 21:
                sum += card + 10
            else:
                sum += card
        else:
            if hasAce == True and sum + 20 >= 17 and sum + 20 <= 21:
                sum += 20
            else:
                sum += 10

        print(f"Your total is now {sum}.")

        if sum >= 21:
              return sum


def giveDealerCards():

    sum = 0
    hasAce = False
    
    while sum < 17:
            
        card = randrange(1, 14)

        if card == 11:
            print("Dealer just drew a Jack.")
        if card == 12:
            print("Dealer just drew a Queen.")
        if card == 13:
            print("Dealer just drew a King.")
        
        if card == 1:
            print("Dealer just drew an Ace.")
            hasAce = True
            if sum + 11 >= 17 and sum + 11 <= 21:
                sum += 11
            else:
                sum += 1
        elif card >= 2 and card <= 10:
            print(f"Dealer just drew a {card}.")
            if hasAce == True and sum + card + 11 >= 17 and sum + card + 11 <= 21:
                sum += card + 10
            else:
                sum += card
        else:
            if hasAce == True and sum + 20 >= 17 and sum + 20 <= 21:
                sum += 20
            else:
                sum += 10

        print(f"Dealer total is now {sum}.")

        if sum >= 17:
              return sum

def printSummary(wins, losses, draws, n):
    print()
    print(f"You won a total of {wins} games.")
    print(f"You lost a total of {losses} games.")
    print(f"You had {draws} drawn games.")
    print(f"Your win rate is {wins/n * 100:.2f}%.")

blackjack()



# Exercise 9.9

# A blackjack dealer always starts with one card showing. It would be useful
# for a player to know the dealer's bust probability (see previous problem)
# for each possible starting value. Write a simulation program that runs
# multiple hands of blackjack for each possible starting value (ace-10) and
# estimates the probability that the dealer busts for each starting value.

def blackjack_dealer_bust_odds():
    printIntro()
    n = simulations()

    for starting_card in range(1, 14):
        busts = 0
        for trial in range(n):
            sum = dealCards(starting_card)
            if sum > 21:
                busts += 1
        print()
        printResults(starting_card, n, busts)

def printIntro():
    print("This program calculates the odds that the dealer will go bust")
    print("based on the value of the starting card.")

def simulations():

    n = 0
    
    while True:
        try:
            n = int(input("How many simulations per card will you execute? "))
            if n <= 0:
                raise Exception
        except ValueError:
            print("Please enter a number.")
            continue
        except Exception:
            print("Please enter a positive integer.")
            continue
        break
    
    return n
    
def dealCards(starting_card):
          
    if starting_card == 1:
        hasAce = True
    else:
        hasAce = False

    if starting_card <= 10:
        sum = starting_card
    else:
        sum = 10
    
    while sum < 17:
            
        card = randrange(1, 14)
        
        if card == 1:
            # print("Dealer just drew an Ace.")
            hasAce = True
            if sum + 11 >= 17 and sum + 11 <= 21:
                sum += 11
            else:
                sum += 1
        elif card >= 2 and card <= 10:
            # print(f"Dealer just drew a {card}.")
            if hasAce == True and sum + card + 10 >= 17 and sum + card + 10 <= 21:
                sum += card + 10
            else:
                sum += card
        else:
            if hasAce == True and sum + 20 <= 21:
                sum += 20
            else:
                sum += 10

        # print(f"Dealer total is now {sum}.")

        if sum >= 17:
            return sum

def printResults(i, n, busts):
    if i == 1:
        print(f"There were {busts} busts out of {n} trials given Ace as the starting card.")
        print(f"{(busts/n) * 100:.2f}% chance.")
    elif i >= 2 and i <= 10:
        print(f"There were {busts} busts out of {n} trials given {i} as the starting card.")
        print(f"{(busts/n) * 100:.2f}% chance.")
    elif i == 11:
        print(f"There were {busts} busts out of {n} trials given Jack as the starting card.")
        print(f"{(busts/n) * 100:.2f}% chance.")
    elif i == 12:
        print(f"There were {busts} busts out of {n} trials given Queen as the starting card.")
        print(f"{(busts/n) * 100:.2f}% chance.")
    elif i == 13:
        print(f"There were {busts} busts out of {n} trials given King as the starting card.")
        print(f"{(busts/n) * 100:.2f}% chance.")


blackjack_dealer_bust_odds()


        
# Exerise 9.12

# A random walk is a particular kind of probabilistic simulation that models
# certain statistical systems such as the Brownian motion of molecules. You
# can think of a one-dimensional random walk in terms of coin flipping.

# Suppose you are standing on a very long straight sidewalk that extends
# both in front of and behind you. You flip a coin. If it comes up heads, you
# take a step forward; tails means to take a step backward.

# Suppose you take a random walk of n steps. On average, how many
# steps away from the starting point will you end up? Write a program to
# help you investigate this question.

def random_walk():

    n = int(input("How many moves would you like to simulate? "))

    steps = 0 # number of steps forward or backward
    
    for i in range(n):
        if random.random() < 0.5:
            steps += 1
        else:
            steps -= 1
    

    if steps > 0:
        print(f"You moved {steps} spaces forward.")
    elif steps < 0:
        print(f"You moved {steps * -1} spaces backward.")
    else:
        print("You are in the starting position.")
        


random_walk()



# Exercise 9.14

# Write a graphical program to trace a random walk (see previous two problems)
# in two dimensions. In this simulation you should allow the step to
# be taken in any direction. You can generate a random direction as an angle
# off of the x axis.
# angle = random() * 2 * math.pi

# The new x and y positions are then given by these formulas:
# x = x + cos(angle)
# y = y + sin(angle)

# The program should take the number of steps as an input. Start your
# walker at the center of a lOOxlOO grid and draw a line that traces the walk
# as it progresses.

def random_walk_360_degrees():

    n = int(input("How many steps would you like to take? "))

    x = 0
    y = 0
    
    for i in range(n):

        # Directions: Calculated based on angle

        angle = random.uniform(0, 1) * 2 * math.pi
        # print(f"{angle} radians")
        # print(f"{degrees} degrees")
        
        x = x + math.cos(angle)
        y = y + math.sin(angle)

    print(f"{x}, {y}")

random_walk_360_degrees()
    



# Exercise 9.15

# Suppose you are located at the exact center of a cube. If you could look
# all around you in every direction, each wall of the cube would occupy 􀀗
# of your field of vision. Suppose you move toward one of the walls so that
# you are now halfway between it and the center of the cube. What fraction
# of your field of vision is now taken up by the closest wall? Hint: Use a
# Monte Carlo simulation that repeatedly "looks" in a random direction and
# counts how many times it sees the wall.

def analytic_geometry_cube_vision():

    n = 5000
    hits = 0

    for i in range(n):
        
        u = random.uniform(-2, 2)
        v = random.uniform(-2, 2)
        w = random.uniform(-2, 2)

        if (u > 0 and abs(v) < (2 * u) and abs(w) < (2 * u)):
            hits += 1

    return hits/n

fraction = analytic_geometry_cube_vision()
    
print("The fraction of your field of vision taken up by the closest wall is")
print(f"{fraction}")

"""
