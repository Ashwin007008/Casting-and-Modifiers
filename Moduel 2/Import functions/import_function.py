import random # Importing the random module
secret = random.randint(1, 5) # Random number between 1 and 5
print("Welcome to the Number Guessing Game!")
while True:
    guess = int(input("Enter your guess (1-5): "))
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break #For loop function


