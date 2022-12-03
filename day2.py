file1 = open('day2.txt', 'r')
Lines = file1.readlines()

# A for Rock, B for Paper, and C for Scissors
ROCK = "A"
PAPER = "B"
SCISSORS = "C"
# X for Rock, Y for Paper, and Z for Scissors
#Y means you need to end the round in a draw, and Z means you need to win
ROCK_R = "X"
PAPER_R = "Y"
SCISSORS_R = "Z"

# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

points = 0

for line in Lines:
    (a, b) = line.strip().split(" ")
    if a == ROCK:
        if b == ROCK_R:
            points += 1+3
        elif b == PAPER_R:
            points += 2+6
        elif b == SCISSORS_R:
            points += 3
        else:
            raise  Exception()
    elif a == PAPER:
        if b == ROCK_R:
            points += 1
        elif b == PAPER_R:
            points += 2+3
        elif b == SCISSORS_R:
            points += 3+6
        else:
            raise  Exception()
    elif a == SCISSORS:
        if b == ROCK_R:
            points += 1+6
        elif b == PAPER_R:
            points += 2
        elif b == SCISSORS_R:
            points += 3+3
        else:
            raise  Exception()
    else:
            raise  Exception()

print(points)
