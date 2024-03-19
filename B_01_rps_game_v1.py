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

# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0


print("💎📃✂ Rock / Paper / Scissors 💎📃✂")
print()

# Instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds do you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    print("you choose infinite")
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("Rounds played: ", rounds_played)

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    print("num_rounds: ", num_rounds)

# Game loop ends here

# Game History / Statistics area
