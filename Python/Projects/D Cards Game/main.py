import random
print("===== Card Distribution Game =====\n")

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace"]

deck = []

for suit in suits:
    for rank in ranks:
        card = rank + " of " + suit
        deck.append(card)

random.shuffle(deck)

player1 = []
player2 = []
player3 = []
player4 = []

for i in range(52):
    if i % 4 == 0:
        player1.append(deck[i])
    elif i % 4 == 1:
        player2.append(deck[i])
    elif i % 4 == 2:
        player3.append(deck[i])
    else:
        player4.append(deck[i])

print("Player 1 Cards:")
print(player1, "\n")

print("Player 2 Cards:")
print(player2, "\n")

print("Player 3 Cards:")
print(player3, "\n")

print("Player 4 Cards:")
print(player4, "\n")