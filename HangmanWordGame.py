## HangmanWordGame.py
##
## This program will initiate a game of "Hangman". The user will have to guess a word (from a pre-determined set of words) randomly chosen when the program starts.
## A hint will be provided.
##
## If the user guesses a letter incorrectly 6 times, the game will end.
##
## Aster Fan
##
## June 2017

import random

wordList = ["hello","testing","seventy","victoria","cauliflower","pineapple","crevasse"] # The word list.
wordHint = ["A greeting","Experimenting","A number","A capital city of a Canadian province","A vegetable","A fruit","A geological feature of a glacier"] # The hint list.
wordChosen = random.choice(wordList)    # This variable will contain the hidden word. It will be shown to the user after the game has ended.

guessesLeft = 5     # This variable will determine the amount of tries the user has. If it reaches less than 0, the game ends.
wordSoFar = ""      # This variable will be the word guessed so far by the user.
wordSoFarCheck = "" # This variable will be the one Python checks for word completion via comparing length.
incorrectLetters = "" # This variable will store incorrect guesses so the user won't guess it again.

# State the intention this program to the user.
print("\nWelcome to Hangman! Guessing 1 letter at a time, try to find out the word!\n")

# The statements below will print out a hint based on the randomly chosen word!
if wordChosen == wordList[0]:
    print("\nYour hint is: {}.".format(wordHint[0]))
elif wordChosen == wordList[1]:
    print("\nYour hint is: {}.".format(wordHint[1]))
elif wordChosen == wordList[2]:
    print("\nYour hint is: {}".format(wordHint[2]))
elif wordChosen == wordList[3]:
    print("\nYour hint is: {}".format(wordHint[3]))
elif wordChosen == wordList[4]:
    print("\nYour hint is: {}".format(wordHint[4]))
elif wordChosen == wordList[5]:
    print("\nYour hint is: {}".format(wordHint[5]))
elif wordChosen == wordList[6]:
    print("\nYour hint is: {}".format(wordHint[6]))

# Begin user guesses quality check.
while True:
    letterGuess = input("The word is {} letters long. You have {} chance(s) to make an incorrect guess. \nEnter your guess!\n> ".format(len(wordChosen),guessesLeft))
    if len(letterGuess) >1:
        print("\nYou are only allowed to guess 1 character at a time. Try again.")
    elif letterGuess.isalpha() == False:
        print("\nAnything other than letters are not allowed. Try again.")
    elif letterGuess.islower() == False:      # Ask for lowercase only
        print("\nOnly lowercase letters are permitted. Try again.")
    else:
        break
    
# .count() method --> used to count how many times a string appears in another string
# .find() method --> used to find the first instance of a string in another string

# The following if-else statement checks for occurences of their chosen letter.
if wordChosen.count(letterGuess) == 0:
    print("\nYour letter, {}, is not in the word!".format(letterGuess))
    incorrectLetters += letterGuess
    guessesLeft -= 1
else:
    print("\nYour letter, {}, appears in the word {} time(s)!".format(letterGuess,wordChosen.count(letterGuess)))

# The following will print out the word so far.
for letter in wordChosen:   # This for loop checks each letter in the wordChosen variable for the letter guessed by the user.
    if letterGuess == letter:
        wordSoFar += " " + letterGuess + " "
        wordSoFarCheck += letterGuess
    else:
        wordSoFar += " _ "
        wordSoFarCheck += ""
        
# This if else statement checks if the user has correctly guessed the word.
if len(wordSoFarCheck) == len(wordChosen):
    print("You have correctly guessed the word!\n\n{}\n".format(wordSoFar))
    
else:
    print("This is what you have so far!\n\n{}\n".format(wordSoFar))

# Reprint the hints for the user.
if wordChosen == wordList[0]:
    print("\nYour hint is: {}.".format(wordHint[0]))
elif wordChosen == wordList[1]:
    print("\nYour hint is: {}.".format(wordHint[1]))
elif wordChosen == wordList[2]:
    print("\nYour hint is: {}".format(wordHint[2]))
elif wordChosen == wordList[3]:
    print("\nYour hint is: {}".format(wordHint[3]))
elif wordChosen == wordList[4]:
    print("\nYour hint is: {}".format(wordHint[4]))
elif wordChosen == wordList[5]:
    print("\nYour hint is: {}".format(wordHint[5]))
elif wordChosen == wordList[6]:
    print("\nYour hint is: {}".format(wordHint[6]))

# User guess quality check.
while True:
    letterGuess = input("The word is {} letters long. You have {} chance(s) to make an incorrect guess. \nEnter your guess!\n> ".format(len(wordChosen),guessesLeft))
    if len(letterGuess) >1:
        print("\nYou are only allowed to guess 1 letter at a time. Try again.")
    elif letterGuess.isalpha() == False:
        print("\nAnything other than letters are not allowed. Try again.")
    elif letterGuess.islower() == False:      # Ask for lowercase only
        print("\nOnly lowercase letters are permitted. Try again.")
    elif letterGuess in wordSoFarCheck or letterGuess in incorrectLetters:      # This statement was added to limit the users guess to unguessed letters.
        print("\nYou have already guessed this letter! Try again.")
    else:
        break
    
# Occurences of chosen letter.
if wordChosen.count(letterGuess) == 0:
    print("\nYour letter, {}, is not in the word!".format(letterGuess))
    incorrectLetters += letterGuess
    guessesLeft -= 1
else:
    print("\nYour letter, {}, appears in the word {} time(s)!".format(letterGuess,wordChosen.count(letterGuess)))

wordSoFar = "" # VERY important as this will allow us to recreate proper placement of the word guessed by user.

for letter in wordChosen:   # This for loop checks each letter in the wordChosen variable for the letter guessed by the user and creates a visual for the user signifying their progress.
    if letterGuess == letter:
        wordSoFarCheck += letterGuess
    if letter in wordSoFarCheck:
        wordSoFar += " " + letter + " "
    else:
        wordSoFar += " _ "

# This if else statement checks if the user has correctly guessed the word.
if len(wordSoFarCheck) == len(wordChosen):
    print("You have correctly guessed the word!\n\n{}\n".format(wordSoFar))
    
else:
    print("This is what you have so far!\n\n{}\n".format(wordSoFar))

if wordChosen == wordList[0]:
    print("\nYour hint is: {}.".format(wordHint[0]))
elif wordChosen == wordList[1]:
    print("\nYour hint is: {}.".format(wordHint[1]))
elif wordChosen == wordList[2]:
    print("\nYour hint is: {}".format(wordHint[2]))
elif wordChosen == wordList[3]:
    print("\nYour hint is: {}".format(wordHint[3]))
elif wordChosen == wordList[4]:
    print("\nYour hint is: {}".format(wordHint[4]))
elif wordChosen == wordList[5]:
    print("\nYour hint is: {}".format(wordHint[5]))
elif wordChosen == wordList[6]:
    print("\nYour hint is: {}".format(wordHint[6]))
    
###### REPEAT BELOW for multiple letter guessing for long word ######
    
# User guess quality check.
while len(wordSoFarCheck) != len(wordChosen):
    while len(wordSoFarCheck) != len(wordChosen):
        letterGuess = input("The word is {} letters long. You have {} chance(s) to make an incorrect guess. \nEnter your guess!\n> ".format(len(wordChosen),guessesLeft))
        if len(letterGuess) >1:
            print("\nYou are only allowed to guess 1 letter at a time. Try again.")
        elif letterGuess.isalpha() == False:
            print("\nAnything other than letters are not allowed. Try again.")
        elif letterGuess.islower() == False:      # Ask for lowercase only
            print("\nOnly lowercase letters are permitted. Try again.")
        elif letterGuess in wordSoFarCheck or letterGuess in incorrectLetters:      # Limit the user guess to unguessed letters.
            print("\nYou have already guessed this letter! Try again.")
        else:
            break
        
# Occurences of chosen letter.
    if wordChosen.count(letterGuess) == 0:
        print("\nYour letter, {}, is not in the word!".format(letterGuess))
        incorrectLetters += letterGuess
        guessesLeft -= 1
    else:
        print("\nYour letter, {}, appears in the word {} time(s)!".format(letterGuess,wordChosen.count(letterGuess)))

    if guessesLeft <0:  # Lose condition
        input("You lose! You guessed too many incorrect letters! Press enter to exit!")
        break
              
    wordSoFar = "" # VERY important to reset variable.

    for letter in wordChosen:   # This for loop checks each letter in the wordChosen variable for the letter guessed by the user.
        if letterGuess == letter:
            wordSoFarCheck += letterGuess
        if letter in wordSoFarCheck:
            wordSoFar += " " + letter + " "
        else:
            wordSoFar += " _ "

# This if else statement checks if the user has correctly guessed the word.
    if len(wordSoFarCheck) == len(wordChosen):
        print("You have correctly guessed the word!\n\n{}\n".format(wordSoFar))
        break
    else:
        print("This is what you have so far!\n\n{}\n".format(wordSoFar))
        if wordChosen == wordList[0]:
            print("\nYour hint is: {}.".format(wordHint[0]))
        elif wordChosen == wordList[1]:
            print("\nYour hint is: {}.".format(wordHint[1]))
        elif wordChosen == wordList[2]:
            print("\nYour hint is: {}".format(wordHint[2]))
        elif wordChosen == wordList[3]:
            print("\nYour hint is: {}".format(wordHint[3]))
        elif wordChosen == wordList[4]:
            print("\nYour hint is: {}".format(wordHint[4]))
        elif wordChosen == wordList[5]:
            print("\nYour hint is: {}".format(wordHint[5]))
        elif wordChosen == wordList[6]:
            print("\nYour hint is: {}".format(wordHint[6]))

