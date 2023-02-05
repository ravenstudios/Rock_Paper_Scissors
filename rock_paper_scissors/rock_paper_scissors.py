"""

The function takes a tuple as an arument with 2 strings, either "Rock", "Paper", "Scissors"
Return which player won as an int. I.E. 1 or 2. Return 0 if it was a draw
"""
def game(choices):

    if choices[0] == choices[1]:
        return 0

    if choices[0] == "Rock":
        if choices[1] == "Paper":
            return 2
        if choices[1] == "Scissors":
            return 1

    if choices[0] == "Paper":
        if choices[1] == "Rock":
            return 1
        if choices[1] == "Scissors":
            return 2

    if choices[0] == "Scissors":
        if choices[1] == "Paper":
            return 1
        if choices[1] == "Rock":
            return 2
