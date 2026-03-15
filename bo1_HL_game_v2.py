import math
import random

# check users enter yes (y) or no (n)
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase

        user_response = input(question).lower()

        for item in valid_ans:

            # check if the user response is a word in the list

            if item == user_response:

                return item

            # check if the user response is the same as

            # the first letter of an item in the list

            elif user_response == item[0]:

                return item

        # print error if user does not enter something that is valid

        print(error)

        print()

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
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"
    # if the number needs to be more than an
    # integer (ie: rounds / "high number")
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f" more than / equal to {low}")
    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()
        # check for infinite mode / exit code
        if response == exit_code:
            return response
        try:
            response = int(response)
            # check response is not too low...
            if low is not None and response < low:
                print(error)
            # check response is more than the low number
            elif high is not None and response > high:
                print(error)
            # if response is valid, return it
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

want_instructions = yes_no("Do you want to read the instructions? ")

#check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Push <enter> for infinite mode: "
                             ,low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 6

# get game parameters
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 1
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
    print("spoiler alert", secret)


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
        if guesses_used == guesses_allowed - 1 and guesses_used == secret:
            print("Careful - you have one guess left!")
    print()
    print("End of rounds")
    # round ends here
    all_scores.append(guesses_used)

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break


    # add round result to game history

    # If user choice is the exit code, break the loop
    rounds_played += 1
    game_history.append(guesses_used)

    user_choice = input("press <enter> to continue or type xxx to quit: ")

    if user_choice == "xxx":
        break


    # Add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"

    # add guesses used to score list
    all_scores.append(guesses_used)

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

    # #display the game history on request
    # see_history = string_checker("Do you want to see the history? ")
    # if see_history == "yes":
    #     for count, item in enumerate(game_history, start=1):
    #         if item <= 2:
    #             print(f"Round {count}: it took you {item} try to get it right!")
    #
    #         else:
    #             print(f"round {count}: it took you {item} trys to get it right!")
    #
    #         else:
    #             if worst_score >= 5:
    #                 feedback = f"round:{count}: you lost this round without any guesses."
    see_history = string_checker("Do you want the game history?")
    if see_history == "yes":
        for count, item in enumerate(game_history, start=1):

            if item == 5:
                print(f"Round {count}: You didnt get the number in time")

            elif item <= 1:
                print(f"Round {count}: it took you {item} try to get it right!")
            else:
                print(f"Round {count}: it took you {item} tries to get it right!")

# if the user have to quit without playing a round, end the program gracefully
else:
    print("🐓🐓🐓 OOPS - NOOOOO!!!!! DONT LEAVE PLEASEEEEEE!!!! 🐓🐓🐓")

    # print(f"{count}: you didnt get it in {item} trys!")