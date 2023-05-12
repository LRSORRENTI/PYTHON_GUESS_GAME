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

# initialize an array to house the code to guess
NUM_CODES = [1, 2, 3, 4, 5]

# define constant variable which contains starting 
# number of attempts
ATTEMPTS = 10

# intitalize the length of the code to four, 
# can also increase value to change difficulty
LENGTH_NUM_CODE = 4

# below function will generate the code 
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
        break;

     return guess