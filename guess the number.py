import random
def guess_the_number():
    print("Welcome to guess the number!")
    print("I have picked a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare guess with the actual number
            if user_guess < number_to_guess:
                print(" Oops Too low! Try again.")
            elif user_guess > number_to_guess:
                print(" Oops Too high! Try again.")
            else:
                print(f" Wohaha Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for playing! Take Care ByeBye.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
