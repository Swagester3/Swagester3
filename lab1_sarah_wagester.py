# Sarah Wagester Week 1 Discussion SDEV 300 6981
""""This program submits your voter registration"""
import sys


def welcome():
    """Displays welcome message"""
    print("\nHello, Welcome to the Python Voter Registration Application.")


def display_output(full_name, age, citizen, state, zipcode):
    """Displays the output"""
    print(f"\n\nThank you, {full_name}, you are successfully registered to vote. ")
    print(f"Age: {age}")
    print(f"U.S. Citizen: {citizen}")
    print(f"State: {state}")
    print(f"Zip code: {zipcode}")
    print("Your voter ID should arrive within 3 weeks.")
    print()
    print("\nThank you for using this program. It will now close, Good-bye!")


def check_citizen(citizen):
    """Function to check U.S. Citizenship"""
    if citizen in ('yes', 'YES', 'Yes', 'yeS', 'yEs', 'YEs', 'YeS', 'yES'):
        return
    if citizen in ('no', 'NO', 'No', 'nO'):
        print("\n***We can only register U.S. citizens at this time.***")
        print("\nThank you for using this program, it will now exit, good-bye!")
        sys.exit()


def check_age(age):
    """Function to check age"""
    if age > 120:
        print("\n***You are probably not over 120 years old, let's try again...")
        (int(input("\nPlease enter your age:    ")))
    elif age < 18:
        print("\n*You are not old enough to vote. Please try again when you turn 18.*")
        print("\nThank you for using this program, it will now exit, good-bye!")
        sys.exit()
    else:
        pass


def check_registered():
    """"Function to check registration"""
    register = (str(input("\nDo you want to continue with Voter Registration? Enter yes or no: ")))
    if register in ('no', 'NO', 'nO', 'No'):
        print("\nThank you for using this program, it will now exit, good-bye!")
        sys.exit()
    else:
        pass


def main():
    """Runs the main program"""
    welcome()

    check_registered()
    first_name = (str(input("\nPlease enter your first name: ")))
    check_registered()
    last_name = (str(input("\nPlease enter your last name:    ")))
    full_name = first_name + " " + last_name
    check_registered()
    age = (int(input("\nPlease enter your age:    ")))
    check_age(age)
    check_registered()
    citizen = (str(input("\nAre you a U.S. citizen?    ")))
    check_citizen(citizen)
    check_registered()
    state = (str(input("\nPlease enter your state of residence:    ")))
    check_registered()
    zipcode = (str(input("\nPlease enter your zip code:    ")))
    display_output(full_name, age, citizen, state, zipcode)


# Execute


main()
