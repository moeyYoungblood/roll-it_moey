import math
import random

# check users enter yes (y) or no (n)

def yes_no(questions):
    while True:
        response = input(questions).lower()

        # check if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please respond with yes / no")


def instructions():
    print('''

to begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the 
secret number will be between 1 and 100

Then choose how many rounds you'd like to play <center> for
infinite mode

your goal is to try to guess the secret number without 
running out of guesses.

 Good luck.

    ''')


# checks for an integer more than 0 (allows <enter>)
def int_check(question, low=None, high=None, exit_code=None):
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

# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# Main Routine Starts here

# Intialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("🔺🔺🔺 Welcome to the higher lower game 🔻🔻🔻")
print()

want_instructions = yes_no("do you want to read the instructions ")

#check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Push <enter> for infinite mode: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# get game parameters
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num+1)

# calculate the maximum number of guesses on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)

    if mode == "infinite":

        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)


    # round starts here
    # set guesses used at the start of each round
    guesses_used = 0
    already_guessed = []

    # choose a 'secret' number between low and high number
    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # Ask the user to guess the number...
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # Check that they don't want to quit
        if guess == "xxx":
            # Set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # Check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses ")
            continue

        # If guess is not a duplicate, add it to the 'already guessed' list
        else:
            already_guessed.append(guess)

        # Add one to the number of guesses used
        guesses_used += 1

        # compare the users guess with secret number

        # if we have guesses left
        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try higher number."
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try lower."
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        elif guess == secret:

            if guesses_used == 1:
                feedback = "lucky! You got it on the first guess."
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
            else:
                feedback = f"well done! you guessed the secreet number in {guesses_used} guesses."

        # if there are no guess left
        else:
            feedback = "Sorry - you have no more guesses. You lose this round!"

        # print тееоаск to user
        print(feedback)

        # Additional Feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1:
            print("\nCareful - you have one guess left!\n")
    print()

    # round ends here
    all_scores.append(guesses_used)

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break


    # add round result to game history

    user_choice = input("press <enter> to continue or type xxx to quit: ")

    # If user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# check user have played at least one round
# before calculating statistics
if rounds_played > 0:
    # game history / statistics area

    # calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # output the statistics
    print("\nSTATISTICS")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2f}")
    print()

    #display the game history on request
    see_history = yes_no("Do you want to see the history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)