
def yes_no(questions):
    while True:
        response = input(questions).lower()

        # check if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please respond with yes / no'")


def instructions():
    print('''

to begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the 
secret number will be between 1 and 100

Then choose how many rounds youd like to play <center> for
infinite mode

your goal is to try to guess the secret number without 
running out of guesses.

 Good luck.

    ''')


# checks for an integer more than 0 (allows <enter>)


def int_check(question):
    while True:

        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode

        if to_check == "":
            return "infinite"

        try:

            response = int(to_check)

            # checks that the number is more than / equal to 1

            if response < 1:

                print(error)


            else:

                return response

        except ValueError:

            print(error)


# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0

print("🔺🔺🔺 Welcome to the higher lower game 🔻🔻🔻")
print()

want_instructions = yes_no("do you want to read the instructions")

#check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode


num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"

    num_rounds = 5

# Game loop starts here


while rounds_played < num_rounds:

    # Rounds headings (based on mode)

    if mode == "infinite":

        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} (Infinite Mode) ♾♾♾"


    else:

        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    print()

    # get user choice

    user_choice = input("Choose: ")

    # If user choice is the exit code, break the loop

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!

    if mode == "infinite":
        num_rounds += 1

