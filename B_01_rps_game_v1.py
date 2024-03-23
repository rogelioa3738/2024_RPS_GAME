import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item on the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Display instructions
def instructions():
    print('''

**** Instructions ****

To begin, choose the number of rounds (or press <enter> for infinite mode).

Then play with the computer. You need to press R (rock), P (papers), S (scissors)

The rules are as follows:
- Paper beats rock
- Rock beats scissors
- Scissors beats paper

Press <xxx> to end the game anytime.

Goodluck!!!
    ''')

# checks for an integer more than 0 (allows <enter>)
def int_check(question):

    while True:

        error = "Please enter and integer that is 1 or more."

        to_check = input(question)

        # check for an infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is greater than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# compares user / computer choice and return
# result win / tie / lose
def rps_compare(user, comp):

    # If the user and computer choice is the same, it's a tie.
    if user == comp:
        result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # If it's not a win / tie, then it's lose
    else:
        result = "lose"

    return result


# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print()
print("💎📃✂ Rock / Paper / Scissors 💎📃✂")
print()

# ask the user if they want to see the instructions and display
# then if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()


# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


print("💎📃✂ Rock / Paper / Scissors 💎📃✂")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds do you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played} (Infinite mode) "
    else:
        rounds_heading = f"\n 🕐🕐🕐 Round {rounds_played + 1} of {num_rounds} 🕐🕐🕐"

    print(rounds_heading)

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choose:", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You choose:", user_choice)


    # if user choice is exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game History / Statistics area
