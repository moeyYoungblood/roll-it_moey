import random

from c_04_round_v1 import double_user


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player}   - roll 1: {roll_one} \t| roll 2: {roll_two} \t|total: {total}")

    return total, double

# roll the dice for the user and note if they got a double
initial_user = initial_points("user")
initial_comp = initial_points("comp")

print("initial_user", initial_user)
print("initial_computer", initial_comp)


# retrieve user points (first item returned from the function.)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]


# let the user know if they qualify for double points
if double_user == "yes":
   print("great news - if you win, you will earn double points!")


