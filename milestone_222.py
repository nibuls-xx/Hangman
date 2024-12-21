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

    # Step 1: Check if the guessed letter is in the word
    if user_letter in word:
      # Step 2: Print success message
      print(f"Good guess! '{user_letter}' is in the word.")
    else:
      # Step 3: Print failure message
      print(f"Sorry, '{user_letter}' is not in the word. Try again.") 

    # Check for win condition
    if all(letter in guessed_letters for letter in word):
      print(f"Congratulations! You guessed the word: {word}")
      break

if __name__ == "__main__":
  play_game()