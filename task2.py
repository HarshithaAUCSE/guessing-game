import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Loop until the user guesses the correct number
    while not guessed_correctly:
        # Ask the user to input their guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is too high, too low, or correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")

# Run the game
guessing_game()
