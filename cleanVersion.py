import hello_world
import random


COLORS = ["R", "G", "B", "Y", "W", "O"]

TRIES = 10

CODE_LENGTH = 4

def generate_Code():
      code = []
      for _ in range(CODE_LENGTH):
            color = random.choice(COLORS)
            code.append(color)
      return code

def guess_Code():
       while True: 
        guess = input("""
        
        Guess: """).upper().split(" ")

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

def check_Code(guess, real_code):
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
    
def determine_Winner():
      print(f"""             This is a code guessing game, you have {TRIES} attempts to guess
             the input. The 'Guess:' key input should follow this structure:

             R G B Y + Enter / Return 

             The valid characters to guess are:""", *COLORS)

      code = generate_Code()

      for attempts in range(1, TRIES + 1):
        guess = guess_Code()
        
        correct_pos, incorrect_pos = check_Code(guess, code)

        if correct_pos == CODE_LENGTH:
         print(f"You guess the code in {attempts} attempts!")
         break
        
        print(f"""
            ________________________________
            Correct Positions: {correct_pos} 
            ________________________________
            Incorrect Positions {incorrect_pos}
            
            """)

      else: 
          print("You ran out of attempts! The code was:", *code  )

      if __name__ == "__main__":
      # the above confirms we're directly running 
      # the python file
        determine_Winner()

determine_Winner()

