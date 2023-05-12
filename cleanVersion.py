import random

NUM_CODES = [1, 2, 3, 4, 5]

ATTEMPTS = 10

LENGTH_NUM_CODE = 4

def generateCode():
      myCode = []
      for _ in range(LENGTH_NUM_CODE):
            number = random.choice(NUM_CODES)
            myCode.append(number)
            return myCode

def guessCode():
       while True: 
        guess = input("Guess: ").split(" ")
        if len(guess) != LENGTH_NUM_CODE:
              print(f"Error: Guess input requires {LENGTH_NUM_CODE} numbers")
              continue
        for number in guess:
             if number not in NUM_CODES:
              print(f"Invalid number: {number}. Try again")
              break
        else:
            break;
       return guess

def checkCode(code):
    correct_code = "1234"
    if code == correct_code:
        return True
    else:
        return False
    
def determineWinner():
      print(f"Code guessing game, you have {ATTEMPTS} to guess correctly")
      print("The valid nunbers to guess are:", *NUM_CODES)
      myCode = generateCode()
      for attempts in range(1, ATTEMPTS + 1):
        guess = guessCode()
        
        correctPosition, incorrectPosition = checkCode(guess, myCode)

        if correctPosition == LENGTH_NUM_CODE:
         print(f"You guess the code in {attempts} attempts!")
            
         break
        print(f"Correct Positions: {correctPosition} | Incorrect Positions {incorrectPosition}")

      else: 
          print("You ran out of attempts! The code was:", *myCode  )

      if __name__ == "__main__":
      # the above confirms we're directly running 
      # the python file
       determineWinner()