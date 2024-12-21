import random


# list of your 5 favorite fruits
fruits = ["apple", "banana", "mango", "strawberry", "grape"] 

# Assign the list to a variable called word_list
word_list = fruits

# Choose a random word from the list
word = random.choice(word_list)

# Get user input for a single letter
guess = input("Enter a single letter: ") 

# Create conditional checks for valid input
if len(guess) == 1 and guess.isalpha(): 
    # Print a message if the input is valid
    print("Good guess!") 
else:
    # Print an error message if the input is invalid
    print("Oops! That is not a valid input.") 

# Print the randomly chosen word
print(word) 