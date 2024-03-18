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

Goodluck!!!
    ''')

# Main routine
print()
print("💎📃✂ Rock / Paper / Scissors 💎📃✂")
print()

# ask the user if they want to see the instructions and display
# then if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")

