from enum import Enum


Rock = 1
Paper = 2
Scissors = 3

Win = 6
Lose = 0
Draw = 3

vals = {
        "A": Rock,
        "B": Paper,
        "C": Scissors,
        "X": Rock,
        "Y": Paper,
        "Z": Scissors,
        }

def wins(them, us):
    # could use a lookup table or something with comparison operators, but w/e
    if them == Rock:
        if us == Rock:
            return Draw
        if us == Paper:
            return Win
        if us == Scissors:
            return Lose
    if them == Paper:
        if us == Rock:
            return Lose
        if us == Paper:
            return Draw
        if us == Scissors:
            return Win
    if them == Scissors:
        if us == Rock:
            return Win
        if us == Paper:
            return Lose
        if us == Scissors:
            return Draw


def score(them, us):
    """
    Your total score is the sum of your scores for each round.
    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    Opponent    | You
    ------------------
    A           | Y
    B           | X
    C           | Z

    This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
    In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

    >>> score("A", "Y")
    8
    >>> score("B", "X")
    1
    >>> score("C", "Z")
    6
    """
    them = vals[them]
    us = vals[us]
    won = wins(them, us)

    return won + us



if __name__ == "__main__":
    import doctest
    doctest.testmod()


with open("input") as f:
   inp = f.read().strip()
print(sum(map(lambda x: score(*x.split()), inp.split("\n"))))

