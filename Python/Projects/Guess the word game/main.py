import random as rnd
words = ['SEVEN', 'SNAKE', 'APPLE', 'MANGO', 'TOMB', 'JERRY', 'HELLO' , 'HAPPY', 'BREAK']
print("--------Guess the Word Game---------------")
print("You Have 10 chances to win the game\nYou have to guess the secret word using letters\nThe letters will be placed automatically on the place if correct\nLet's Start----->")

word = rnd.choice(words)

dash = ['_' for i in range(len(word))]
def display():
    for i in dash:
        print(i,end='')
    print("\n")
display()
win = True
find = []
for i in range(10):
    updash = "".join(dash)
    if updash == word.lower():
        print("Congrats you won !!")
        break
    count=i
    choice = str(input("Enter a character : "))
    if choice.upper() in word:
        find = [i for i in range(len(word)) if word[i] == choice.upper()]
        for i in find:
            dash[i]=choice
        display()
        print("\nCorrect !!")
    else:
        display()
        print("Try again !!")
if count == 9 and updash != word:
    print("Your Chances are over ! Game lost")
    print("The word was:", word)