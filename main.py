
# initialise list to hold game history
game_history = []

# gte data (base component does thi already, code for testing purposes)
user_score = 0
comp_score = 0

while True:
    rounds_played = input("round? ")
    if rounds_played == "":
        break

    user_points = int(input("user point?"))
    comp_points = int(input("computer point?"))
    winner = input("who won?")
    user_score = int(input("user score:"))
    comp_score = int(input("computer score:"))

    game_results = (f"Rounds {rounds_played}: User points {user_points} |"
                    f" computer points {comp_points}, {winner} wins (15 | 0"
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)


print("game history")

for item in game_history:
    print(item)
    






