# first import the random module 

# The random module in Python is a 
# built-in module that provides a 
# random number generator. It can be 
# used to generate random numbers, shuffle lists,
# and perform other random operations. The
# random module is a powerful tool that can 
# be used for a variety of tasks, such as:

# Generating random numbers for
#  games and simulations
# Shuffling lists of data
# Creating random passwords
# Generating random strings
# Performing other random operations
# The random module is easy to use. 
# To generate a random number, you 
# can use the random() function. For 
# example, the following code will 
# generate a random number between 0 and 10:

# number = random.randint(0, 10)
# Use code with caution. Learn more
# The random module also provides a
#  variety of other functions for
#  generating random numbers, such as:

# randrange(): Generate a random 
# number within a specified range

# choice(): Choose a random element from a list

# shuffle(): Shuffle a list in place

# sample(): Return a random sample of 
# elements from a list

# The random module is a powerful
#  tool that can be used for a
#  variety of tasks. If you are
#  looking for a way to generate 
# random numbers in Python, the 
# random module is a great option.
import random

# Note: In Python, when naming constants, it's 
# normal convention to name a constant variable
# using all uppercase like: MYCONSTVAR = 1 
# MYCONSTVAR should never change

# initialize an array to house the code to guess
NUM_CODES = [1, 2, 3, 4, 5]

# define constant variable which contains starting 
# number of attempts
ATTEMPTS = 10

# intitalize the length of the code to four, 
# can also increase value to change difficulty
LENGTH_NUM_CODE = 4

# below function will generate the code 
# note in python, 'def' is used prefixed to functions
# this keyword is married to functions exclusively
# you would never prefix 'def' to anything other than 
# function declarations
def generateCode():
    # first set code to empty list, in python 
    # list is a data structure that can store a 
    # collection of items. Items in a list can be
    # of any type, including strings, integers, 
    # floats, and objects. Lists are ordered, 
    # which means that the items in a list have
    # a specific position. Lists are mutable, which
    # means that the items in a list can be changed.
    myCode = []
    # below use a loop, utilizing an _ to signify that 
    # it doesn't matter what iteration it's on, an anonymous 
    # variable 
    for _ in range(LENGTH_NUM_CODE):
        # below we use that random module we imported 
        # to get a random number from NUM_CODES
        number = random.choice(NUM_CODES)
        # then append that num using .append
        myCode.append(number)
    return myCode

# As an additional note, apparently Python requires indentation
# as a language requirement to structure code 
# instead of curly braces Python uses
# indentation... seems foreign but ok
print("hello world")
def guessCode():
    # now we need to implement the guessing 
    #  functionality, we can do this using the input 
    #  function
    
    # Up first we set up a while loop, in case there 
    # is not a valid guess, it will loop until there is 
    while True: 
     guess = input("Guess: ").split(" ")
    # the above will convert the entry field from 
    # "1 2 3 4" -> [1, 2, 3, 4]

    # we also need a conditional check to see if 
    # this list length is equal to four 

     if len(guess) != LENGTH_NUM_CODE:
       # also note string interpolation in Python is 
       # used by prefixing 'f' before string, then 
       # just like template literals in JS it's 
       # {variableName}
       print(f"Error: Guess input requires {LENGTH_NUM_CODE} numbers")
       # below add continue, which brings us to the top 
       # of the loop
       continue
     
     # we also need a check for whether or not the guess 
     # includes valid numbers to be guessed

     for number in guess:
        # implement check to see if number is valid
        if number not in NUM_CODES:
           print(f"Invalid number: {number}. Try again")
           break
        # if we make it past the break statement, that 
        # means the numbers in the input field were valid
     else:
        # the below will break out of the while loop
        break;

     return guess
    
# now we need a way to check the code: 

def checkCode(guess, realCode): 
   # this is where we're going to check the numbers
   # to see how many are correct
   # Step 1 is check which numbers are in the correct
   # postion

   # Step 2 is to check which numbers are in the incorrect 
   # position

   # The checking order is required, otherwise we could 
   # double count the number
   
   # First we define numberCounts to a dictionary

   numberCounts = {

   }

   # Then we declare a variable for correct position:

   correctPosition = 0

   # Then we declare a variable for incorrect position:

   incorrectPosition = 0

# then we need to use a forloop to keep track of the counts 
# of all of the numbers, do we have two '1's or one '3' etc..
# We'll then store that in the color counts dictionary
   for number in realCode:
      if number not in numberCounts:
         # if number is not a key in dictionary,
         # add it
         numberCounts[number] = 0
      numberCounts[number] += 1
# Below we have a loop, and a function called zip
# what zip does is combine the arguments passed in,
# in our case: guess and realCode, and combine 
# them into tuples, and return a list of them
   for guessNumber, realNumber in zip(guess, realCode):
      if guessNumber == realNumber:
         # the above will check if a guessed number
         # is correct at the same position
         correctPosition += 1
         # then we decrease the count from the 
         # number counts dictionary with -=
         # because we need to indicate that this 
         # number we just found is in the correct 
         # position, that way we don't count it with 
         # the colors in the incorrect position
         numberCounts[guessNumber] -= 1
   for guessNumber, realNumber in zip(guess, realNumber):
      if guessNumber in numberCounts and numberCounts[guessNumber] > 0:
         # for example if we have: 
         # real[3, 1, 1, 1]
         # guess[3, 2, 2, 2]
         # we need to indicate to the user that 
         # they have one number in the correct index,
         # and zero in the incorrect position
         incorrectPosition += 1
         # then we subtract the number counts
         numberCounts[guessNumber] -= 1
         # Now we don't return that another number is in 
         # the incorrect position
      return correctPosition, incorrectPosition
   
   # Now we have the three main components of our game
   # we need to now link them together with logic