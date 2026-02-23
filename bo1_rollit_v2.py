import random

def yes_no(question):

    """check the user says yes / no / y / n, returns 'yes or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no / y / n
        if response == "yes" or response == "y":
           return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print ("say yes / no")

def instructions():
    """Print instructions"""

    print("""
*** instructions *** 

roll the dice and try to win!
    """)

def int_checker():


    error = "please enter an integer more than / equal to 13"

    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)



def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two

    return total, double


def make_statement(statement, decoration):
    """adds emoji / additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


# main starts here....


# at the start of the game, computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []


make_statement("welcome ro the roll it 13 game", "🍀")

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("does selu like kava? ")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_checker()

# play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    #start of round loop
    make_statement(f"round {rounds_played}", "🎲")
    # roll the dice for the user and note if they got a double
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # retrieve user points (first item returned from the function.)
    user_points = initial_user[0]
    comp_points = initial_comp[0]

    double_user = initial_user[1]

    # let the user know if they qualify for double points
    if double_user == "yes":
        print("great news - if you win, you will earn double points!")

    # assume user goes first
    first = "user"
    second = "computer"
    player_1_points = user_points
    player_2_points = comp_points

    # if the user has fewer points, they start the game
    if user_points < comp_points:
        print("you start because your initial roll was less than the computer roll")


    # if the user and computer roll equal points, the users is player 1...
    elif user_points == comp_points:
        print("the initial rolls were the same, the  user starts")

    #  if the computer has fewer points, switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # loop until we have a winner...
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round\n")

        # first person rolls the dice and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{second}: rolled a {player_1_roll} - has {player_1_points} points")

        #    if the first persons score is over 13, end the round
        if player_1_points < 13:
            break

        #    second person rolls the die (score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}:    Rolled a {player_2_roll} - has {player_2_roll} points")

        print(f"{first}: {player_1_roll}   |  {second} {player_2_points}")

    #     end of round

    # associate plater points with either the user or the computer
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and the computer points if the computer went first
    user_points = player_1_points
    comp_points = player_2_points

    # switch the user and computer points if the computer went first
    if user_points > comp_points:
        winner = "User"
        loser = "computer"
        comp_points = 0
    else:
        winner = "Computer"
        loser = "user"
        user_points = 0

    round_feedback = f"the {winner} won."

    # double user points if eligible
    if winner == "User" and double_user == "yes":
        user_points = user_points * 2

    #     output round results
    make_statement("round results", "=")
    print(f"user_points: {user_points} | computer points: {comp_points}")
    print(round_feedback)
    print()

    # Outside rounds loop - Update score with round points, only add points to the score of the
    comp_score += user_points
    user_score += user_points

    # generate round results and add it to the game history list
    game_results = (f"Rounds {rounds_played}: User points {user_points} |"
                    f" computer points {comp_points}, {winner} wins (15 | 0"
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)



    # Show overall scores (add this to rounds loop)
    print("*** Game Update ***")  # Replace with call to statement generator
    print(f"User Score: {user_score} | Computer Score: {comp_score}")

# End of entire game, output final results

make_statement("game over","🏁")

print()
if user_score > comp_score:
        make_statement("the user won", "👍") # Replace this with statement generator call
else:
    make_statement("The Computer won", "💻")

print()
make_statement("game history","🎲")

for item in game_history:
    print(item)