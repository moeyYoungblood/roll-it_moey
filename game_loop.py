# at the start of the game, computer / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("game goal"))

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    #start of round loop
    # for testing purposes, ask the user what the points for the user computer
    comp_score = int(input("enter the computer points at the end of the round"))
    user_points = int(input("enter the points at the end of the round"))

    # Outside rounds loop - Update score with round points, only add points to the score of the
    comp_score += user_points
    user_score += user_points
    # Show overall scores (add this to rounds loop)
    print("*** Game Update ***")    # Replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score: {comp_score}")

# End of entire game, output final results
print()
if user_score > comp_score:
    print("The User won")   # Replace this with statement generator call
else:
    print("The Computer won")