import random

print("===== Guess The Number Game =====")
print("Computer think one number between 1 to 100")
print("You have 10 chance to guess it")
print("Score start from 100 and reduce by 10 each wrong try\n")

secret = random.randint(1, 100)
chance = 10
score = 100
while chance > 0:
    print(f"Chances left: {chance}")
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Correct guess!")
        print(f"Your score is: {score}")
        break
    elif guess > secret:
        print("Hint: Choose a Lower Number")
    else:
        print("Hint: Choose a Higher Number")
    chance -= 1
    score -= 10
    print()

if chance == 0:
    print("Game Over")
    print(f"Correct number was: {secret}")