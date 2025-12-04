
import random
import math

def play_guessing_game():
    """
    Implements a number guessing game based on the provided algorithm.
    """
    print("Welcome to the Number Guessing Game!")

    # 1. Accept lower and upper bounds from the user.
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))

            if lower_bound >= upper_bound:
                print("Error: The lower bound must be less than the upper bound. Please try again.")
            else:
                break # Exit loop if bounds are valid
        except ValueError:
            print("Invalid input. Please enter whole numbers for the bounds.")

    # 2. Generate a random number in the selected range.
    secret_number = random.randint(lower_bound, upper_bound)
    print(f"\nI've picked a number between {lower_bound} and {upper_bound}.")

    # 3. Calculate the maximum allowed guesses using the binary search formula.
    # The formula is log2(N), where N is the range size (upper_bound - lower_bound + 1)
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    print(f"You have a maximum of {max_guesses} guesses.")

    attempts_made = 0
    
    # 4. Run a loop to take user guesses:
    while attempts_made < max_guesses:
        try:
            guess = int(input(f"Guess #{attempts_made + 1}: Enter your guess: "))
            attempts_made += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts_made} attempts!")
                break # Exit the loop if guess is correct
            elif guess < secret_number:
                print("Try Again! You guessed too small.")
            else: # guess > secret_number
                print("Try Again! You guessed too high.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            # Do not increment attempts_made for invalid input

    # 5. If the user runs out of chances
    else: # This 'else' block executes if the while loop completes without a 'break'
        print("\n--- Game Over ---")
        print(f"Better Luck Next Time! The number I was thinking of was {secret_number}.")

# To run the game, call the function:
if __name__ == "__main__":
    play_guessing_game()
