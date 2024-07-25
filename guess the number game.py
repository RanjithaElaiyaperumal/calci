import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    
    if difficulty == "easy":
        number_to_guess = random.randint(1, 50)
        max_attempts = 10
    elif difficulty == "medium":
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
    elif difficulty == "hard":
        number_to_guess = random.randint(1, 200)
        max_attempts = 5
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
    
    attempts = 0
    score = 0
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            score = 100 - (attempts * (100 // max_attempts))
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"Your score is: {score}")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
