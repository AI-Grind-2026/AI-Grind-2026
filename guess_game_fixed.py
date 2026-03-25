import random

# Main game loop
while True:
    number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess a number between 1 and 10: "))
            attempts += 1

            if guess == number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
            elif guess > number:
                print("Too high! Try again.")
            elif guess < number:
                print("Too low! Try again.")
        except ValueError:
            print("Please enter a valid number!")
            continue  # Don't count invalid input as attempt

    else:  # No break, max attempts reached
        print(f"Game over! The number was {number}. Better luck next time!")

    # Ask to play again (line ~19 equivalent fixed)
    replay = input("Do you want to play again? (yes/no): ").lower().strip()
    if replay != "yes":
        print("Thanks for playing!")
        break

print("Goodbye!")
