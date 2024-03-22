"""Guess the Number

1. The program should generate a random number within a specified range (e.g., 1-100).
2.The user should be prompted to guess the number.
3.After each guess, the program should provide feedback to the user if the guess is too high or too low.
4.The user should have a limited number of attempts (e.g., 7 or 10).
5.If the user guesses the correct number, the program should display a congratulatory message.
6. If the user runs out of attempts, the program should reveal the correct number and display a "better luck next time" message.
7. The program should allow the user to play again or exit after each game."""
import random

def guess_number():
    while True:
        # Generate a random number between 1 and 100
        guess_val = random.randint(1, 100)
        total_attempts = 7  # Number of total attempts allowed
        to_guess = set()  # Initialize an empty set to track to guesses

        print("\nHi! Welcome Player!")
        print("Think of a number between 1 and 100 and give me...")

        while total_attempts > 0:
            print("\n Guess again you have ", total_attempts, "more attempts left.")
            
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue  # Skip to the next iteration of the loop

            # Check if the guess is unique
            if guess in to_guess:
                print("Rechecked the number",guess,"lost a chance")
                print("\n Guess again you have ", total_attempts, "more attempts left.")
                continue  # Skip to the next iteration of the loop
            else:
                to_guess.add(guess)  # Add the guess to the set

            if guess == guess_val:
                print(f"Congratulations! you won the game the correct guess - {guess_val}")
                break
            elif guess < guess_val:
                print("Too LOW! try with higher numbers than your guess:",guess)
            else:
                print("Too HIGH! try with lower numbers than your guess",guess)

            total_attempts -= 1

        if total_attempts == 0:
            print("\nSorry,you're very close TRY AGAIN!")
            print(f"The correct number is: {guess_val}")

        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again != 'y':
            print("Thanks for playing.Better luck next time.Visit again!!!")
            break

if __name__ == "__main__":
    guess_number()
