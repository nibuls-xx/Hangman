import random

def get_valid_letter():
  """
  Prompts the user for a single letter and validates the input.

  Returns:
    str: The valid single letter entered by the user.
  """
  while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
      return guess
    else:
      print("Invalid letter. Please, enter a single alphabetical character.")

def play_game():
  """
  Plays a simple word guessing game.
  """
  fruits = ["apple", "banana", "mango", "strawberry", "grape"] 
  word_list = fruits
  word = random.choice(word_list)
  guessed_letters = []

  while True:
    user_letter = get_valid_letter()

    if user_letter in guessed_letters:
      print("You already guessed that letter.")
      continue

    guessed_letters.append(user_letter)

    if user_letter in word:
      print(f"Good guess! '{user_letter}' is in the word.")
    else:
      print(f"Sorry, '{user_letter}' is not in the word.")

    # Check for win condition (implement later)

    # Display hints (implement later)

if __name__ == "__main__":
  play_game()