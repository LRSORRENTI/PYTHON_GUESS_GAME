import random


COLORS = ["R", "G", "B", "Y", "W", "O"]

TRIES = 10

CODE_LENGTH = 4

def generateCode():
      code = []
      for _ in range(CODE_LENGTH):
            color = random.choice(COLORS)
            code.append(color)
      return code

def guessCode():
       while True: 
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
              print(f"Error: Guess input requires {CODE_LENGTH} colors")
              continue
        for color in guess:
             if color not in COLORS:
              print(f"Invalid color: {color}. Try again")
              break
        else:
            break;
       return guess

def checkCode(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
            color_counts[color] += 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos
    
def determineWinner():
      print(f"Code guessing game, you have {TRIES} to guess correctly")
      print("The valid nunbers to guess are:", *COLORS)

      code = generateCode()

      for attempts in range(1, TRIES + 1):
        guess = guessCode()
        
        correct_pos, incorrect_pos = checkCode(guess, code)

        if correct_pos == CODE_LENGTH:
         print(f"You guess the code in {attempts} attempts!")
         break
        
        print(f"Correct Positions: {correct_pos} | Incorrect Positions {incorrect_pos}")

      else: 
          print("You ran out of attempts! The code was:", *code  )

      if __name__ == "__main__":
      # the above confirms we're directly running 
      # the python file
        determineWinner()

determineWinner()

