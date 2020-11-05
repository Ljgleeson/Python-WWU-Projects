#Liam Gleeson
# 5/22/18
# File: lotterySimulation.py
# WWU Comqqewrputer Science
# CSCI 141

# import the random module
import random

# Generate the "winning" pick, which is
# a word and the digit 1, 2 or 3. The word
# or digit can be first
def generateWinningPick():

    # generate the random integer 1, 2 or 3
    aRandomInteger = random.randrange(1,4)

    # Select one of three words, and return
    # the winning pick, which is a concatenation
    # of the word and the str equivalent
    # of aRandomInteger
    anotherRandomNum = random.randrange(1,6)
    if (anotherRandomNum == 1):
        return "monkey" + str(aRandomInteger)
    elif (anotherRandomNum == 2):
        return "dragon" + str(aRandomInteger)
    elif (anotherRandomNum == 3):
        return "snake" + str(aRandomInteger)
    elif (anotherRandomNum == 4):
        return str(aRandomInteger) + "dragon"
    elif (anotherRandomNum == 5):
        return str(aRandomInteger) + "monkey"
    else:
        return str(aRandomInteger) + "snake" 
# the main function
def main():
    # generate the winning lottery pick
    winningPick = generateWinningPick()
    # print welcome message
    print("Lottery pic checker V1.2. Let's see if you've won")
    print("a fabulous prize. The word choices were monkey,")
    print("dragon, and snake, and digit choices were 1, 2 or 3.")
    print("The winning pick is a word and digit, in any order.")
    #The input for guessing a word/number
    guess = input("What word/number combination did you select")
    #two if statements to make sure the variables are those that are required
    if "monkey" not in guess and "snake" not in guess and "dragon" not in guess:
        print("Your input MUST contain one of the words monkey, dragon, or snake")
    if "1" not in guess and "2" not in guess and "3" not in guess:
        print("Your input MUST contain one of the numbers 1, 2, or 3")
    numEntered = ""
    wordEntered = ""
    #two if statements to catergorize what numEntered and wordEntered should be
    if guess[0] == "1" or guess[0] == "2" or guess[0] == "3":
        numEntered = guess[0]
        wordEntered = guess[1:]
    if guess[0] == "m" or guess[0] == "d" or guess[0] == "s":
        numEntered = guess[-1]
        wordEntered = guess[0:-1]
    #from having the wordEntered and numEntered, we can make if, elif statements that check if its "in" or "not in" the statement.
    if guess == winningPick:
        print("You guessed the right number and word. You win the big bucks, Woo Hoo.")
        
    elif numEntered in winningPick[-1] and wordEntered in winningPick[0:-1] or numEntered in winningPick[0] and wordEntered[1:]:
        print("You guessed the right word and right number, but in the wrong order")
        
    elif numEntered in winningPick[0] or numEntered in winningPick[-1]:
        print("You guessed the right number but not the right word.")
        
    elif wordEntered in winningPick[0:-1] or wordEntered in winningPick[1:]:
        print("You guessed the right word but not the right number")
        
    elif guess not in winningPick:
        print("You guessed neither the word nor number.")
        
    print("The winning pick was", winningPick)
       
main()
