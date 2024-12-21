import random

def get_valid_letter():
  """Prompts the user for a single letter and validates the input.

  Returns:
    str: The valid single letter entered by the user.
  """
  while True:
    guess = input("Enter a single letter: ").lower() 
    if len(guess) == 1 and guess.isalpha():
      return guess
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

def check_letter_in_word(guess, word):
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

def get_user_input_and_check_guess(word):
  """
  Gets user input and checks if the guess is in the word.

  Args:
    word: The secret word.

  Returns:
    bool: True if the guess is correct, False otherwise.
  """
  guess = get_valid_letter()
  return check_letter_in_word(guess, word)

def display_current_word(word, guessed_letters):
  """
  Displays the current state of the word, 
  revealing guessed letters and hiding others with underscores.

  Args:
    word: The secret word.
    guessed_letters: A list of guessed letters.

  Returns:
    str: The current state of the word, e.g., "_ a _ p _ e".
  """
  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += letter
    else:
      display += "_"
  return display

def play_game():
  """
  Plays a simple word guessing game.
  """
  word_list = ["apple", "banana", "mango", "strawberry", "grape"] 
  word = random.choice(word_list)
  guessed_letters = []
  lives = 6 

  print("Welcome to Hangman!")
  print("-" * 20)

  while lives > 0:
    print(f"Lives remaining: {lives}")
    print(display_current_word(word, guessed_letters)) 

    if get_user_input_and_check_guess(word): 
      guessed_letters.append(user_letter) 

    # Check for win condition
    if all(letter in guessed_letters for letter in word):
      print(f"Congratulations! You guessed the word: {word}")
      break

    lives -= 1

  if lives == 0:
    print(f"You lose! The word was: {word}")

if __name__ == "__main__":
  play_game()