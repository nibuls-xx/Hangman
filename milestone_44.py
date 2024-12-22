import random

class Hangman:
  """
  A class representing the Hangman game.

  Attributes:
      word: The secret word to be guessed (chosen randomly from word_list).
      word_guessed: A list representing the current state of the word,
                    with '_' for unguessed letters and actual letters for guessed ones.
      num_letters: The number of unique letters in the word that haven't been guessed yet.
      num_lives: The number of lives remaining for the player.
      word_list: A list of words used for random word selection.
      list_of_guesses: A list containing all the letters the player has guessed so far.
  """

  def __init__(self, word_list, num_lives=5):
    """
    Initializes the Hangman game with a random word and default number of lives.

    Args:
        word_list: A list of words used for random word selection.
        num_lives (int, optional): The number of lives the player starts with. Defaults to 5.
    """
    self.word = random.choice(word_list)
    self.word_guessed = ["_" for _ in self.word] 
    self.num_letters = len(set(self.word))  # Count unique letters
    self.num_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  def check_guess(self, guess):
    """
    Checks if the guessed letter is in the word.

    Args:
      guess: The letter guessed by the user.

    Returns:
      bool: True if the guess is in the word, False otherwise.
    """
    guess = guess.lower()
    if guess in self.word:
      print(f"Good guess! '{guess}' is in the word.")
      return True
    else:
      print(f"Sorry, '{guess}' is not in the word. Try again.")
      return False