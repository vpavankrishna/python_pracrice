import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    random_number = random.randint(lower_bound, upper_bound)
    
    # Set the number of attempts
    attempts = 0
    max_attempts = 10

    print(f"Guess the number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == random_number:
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts!")
                break
            elif guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")
        
        # Check if attempts are exhausted
        if attempts == max_attempts:
            print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_number}.")
            break

# Run the game
if __name__ == "__main__":
    number_guessing_game()