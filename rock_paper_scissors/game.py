from rock_paper_scissors import game


choices = ["Rock", "Paper", "Scissors"]


player1_input = int(input("Player 1 choose 0, 1 or 2 Rock Papper Scissors\n"))
print(f"You chose {choices[player1_input]}")
player2_input = int(input("Player 2 choose 0, 1 or 2 Rock Papper Scissors\n"))
print(f"You chose {choices[player2_input]}")
result = game((choices[player1_input], choices[player2_input]))

if result == 0:
    print("Draw")
if result == 1:
    print("Player 1 WON!!!")
if result == 2:
    print("Player 2 WON!!!")
