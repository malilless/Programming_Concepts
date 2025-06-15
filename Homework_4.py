import random
from Homework_4_functions import get_result, get_string_from_results

# Choosing the word
words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
secret_word = random.choice(words)

# Define parameters
tries = 6

# Intro
print("Wecome to Wordle!")
expected_word_length = len(secret_word)
print(f"Guess the {expected_word_length}-letter word. You have {tries} tries.")

# Main cycle
while tries > 0:
    # Get input
    guess = input(f"Attempt {7-tries}/6 - Enter your guess: ").lower()

    # Check input length (tries not consumed)
    if len(guess) != expected_word_length:
        print(f"Wrong length. Expected {expected_word_length} symbols.")
        continue
    
    # Are you lucky?
    if guess == secret_word:
        print(f"You win!!! It's '{secret_word}'.")
        break

    # Get comparision result for every character
    results = get_result(guess, secret_word)

    # Form and output result for the try
    print(f"Result: {get_string_from_results(results, guess)}")

    # Decrease tries left
    tries -= 1
else:
    # Poor looser.....
    print(f"You lose! The word was: '{secret_word}'.")