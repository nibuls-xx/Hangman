import random

def get_valid_letter():
  """
  Prompts the user for a single letter and validates the input.

  Returns:
    str: The valid single letter entered by the user.
  """
  while True:
    guess = input("Enter a single letter: ").lower() 
    if len(guess) == 1 and guess.isalpha():
      return guess
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess, word):
  """
  Checks if the guessed letter is in the word.

  Args:
    guess: The letter guessed by the user.
    word: The secret word.

  Returns:
    bool: True if the guess is in the word, False otherwise.
  """
  if guess in word:
    print(f"Good guess! '{guess}' is in the word.")
    return True
  else:
    print(f"Sorry, '{guess}' is not in the word. Try again.")
    return False

def ask_for_input(word):
  """
  Asks the user for input and checks if the guess is in the word.

  Args:
    word: The secret word.

  Returns:
    bool: True if the guess is correct, False otherwise.
  """
  guess = get_valid_letter()
  return check_guess(guess, word) 

def play_game():
  """
  Plays a simple word guessing game.
  """
  word_list = ["apple", "banana", "mango", "strawberry", "grape"] 
  word = random.choice(word_list)
  guessed_letters = []
  lives = 6  # Number of lives

  print("Welcome to Hangman!")
  print("-" * 20)

  while lives > 0:
    display_word = ""
    for letter in word:
      if letter in guessed_letters:
        display_word += letter
      else:
        display_word += "_"
    print("Current word:", display_word) 

    if ask_for_input(word): 
      guessed_letters.append(user_letter) 

    # Check for win condition
    if all(letter in guessed_letters for letter in word):
      print(f"Congratulations! You guessed the word: {word}")
      break

    lives -= 1
    print(f"Lives remaining: {lives}")

  if lives == 0:
    print(f"You lose! The word was: {word}")

if __name__ == "__main__":
  play_game()