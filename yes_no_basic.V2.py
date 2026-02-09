# function goe here

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

# Main routine

want_instructions = yes_no("does selu like kava? ").lower()
want_kava = yes_no("do you want kava?")

print("we are done")