logo = """

     ______                                 _________  __              ____  _____                       __                       
   .' ___  |                               |  _   _  |[  |            |_   \|_   _|                     [  |                      
  / .'   \_| __   _   .---.  .--.   .--.   |_/ | | \_| | |--.  .---.    |   \ | |  __   _   _ .--..--.   | |.--.   .---.  _ .--.  
  | |   ____[  | | | / /__\\( (`\] ( (`\]      | |     | .-. |/ /__\\   | |\ \| | [  | | | [ `.-. .-. |  | '/'`\ \/ /__\\[ `/'`\] 
  \ `.___]  || \_/ |,| \__., `'.'.  `'.'.     _| |_    | | | || \__.,  _| |_\   |_ | \_/ |, | | | | | |  |  \__/ || \__., | |     
   `._____.' '.__.'_/ '.__.'[\__) )[\__) )   |_____|  [___]|__]'.__.' |_____|\____|'.__.'_/[___||__||__][__;.__.'  '.__.'[___]    
                                                                                                  
"""

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(guess, answer, turns):
  """Check answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attemps remaining to guess the number")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("You've run out of guesses. You lose.")
      return
    elif guess != answer:
      print("Guess Again")

game()
