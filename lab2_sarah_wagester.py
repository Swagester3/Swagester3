# Sarah Wagester Week 1 Discussion SDEV 300 6981
"""This program displays a menu for users to run at the command line
provides and an answer or password dependent on the option chosen
"""

import string
import secrets
from datetime import date
import math


def display_menu():
    """Method to display menu options to user."""
    print("\nPlease choose from one of the following options.\n")
    print("1. Generate a Secure Password")
    print("2. Calculate and format a percentage")
    print("3. How many days from today until July 4th, 2025?")
    print("4. Use the Law of Cosines to calculate the leg of a triangle")
    print("5. Calculate the volume of a Right Circular Cylinder")
    print("9. Exit the program.")


def password_generator():
    """This function generates a secure password"""
    alphabet = string.ascii_letters + string.digits + string.punctuation  # merges strings
    print("\nSpecial characters will be added to any remaining length.")
    length = (int(input("\nPlease indicate the length you would like for your password:     ")))
    if length < 8:  # validates if the length is a higher than 8
        print("\nThe length should be 8 or more, please reenter:   ")
        length = (int(input()))
    upper = (int(input("How many letters need to be upper case?   ")))
    if upper < 0:
        print("This number cannot be negative, please reenter:   ")
        upper = (int(input("How many letters need to be upper case?   ")))
    else:
        pass
    lower = (int(input("How many letters need to be lower case?  ")))
    if lower < 0:
        print("This cannot be a negative number, please renter:   ")
        lower = (int(input("How many letters need to be lower case?  ")))
    else:
        pass
    digit = (int(input("How many digits required?   ")))
    if digit < 0:
        print("This cannot be a negative number, please renter:   ")
        digit = (int(input("How many digits required?   ")))
    else:
        pass
    print("\n****Stand by while we generate your password.****\n")
    while True:  # this while statement creates the password using input supplied
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (sum(c.islower() for c in password) == lower
                and sum(c.isupper() for c in password) == upper
                and sum(c.isdigit() for c in password) == digit):
            print(f"Your requested password with {upper} uppercase letters, {lower} "
                  f"lowercase letters, and {digit} digits is:\n")
            print(password)  # displays password generated
            break


def calculate_percentage():
    """This function calculates and formats a percentage"""
    while True:
        numerator = (float(input("Please enter the Numerator:    ")))  # numerator can be any value
        denominator = (float(input("Please enter the Denominator:     ")))
        if denominator == 0:  # validates if the denominator is a positive value
            print("\nThe denominator should not be 0, please reenter:   ")
            denominator = (float(input()))
        decimal = (int(input("How many decimal places would you like the percentage rounded to? ")))
        if decimal < 0:  # validates if the decimal is a positive value
            print("\nThe decimal place should be a positive number, please reenter:   ")
            decimal = (int(input()))
        percentage = (numerator / denominator) * 100  # calculates percentage
        print()
        print(round(percentage, decimal))  # rounds and displays percentage to the user
        break


def days_until_july_4_2025():
    """This function calculates how many days until July 4th, 2025"""
    print()
    today = date.today()  # populates today's date to store
    july = date(2025, 7, 4)  # sets date to count to
    days_until_july = abs(july - today)  # subtracts future date from today
    print(f"There are {days_until_july.days} days until July 4th 2025.")  # displays days to user


def leg_of_triangle():
    """This function uses the Law of Cosines to calculate the leg of a triangle"""
    while True:
        side_a = (float(input("\nPlease enter the length of side A:    ")))
        if side_a < 0:  # validates length of A is positive number
            print("\nThe length of side A should be a positive number , please reenter: ")
            side_a = (float(input()))
        side_b = (float(input("\nPlease enter the length of side B:    ")))
        if side_b < 0:  # validates length of B is a positive number
            print("\nThe length of side B must be a positive number, please reenter:   ")
            side_b = (float(input()))
        angle_c = float(input("\nPlease enter angle C:    "))
        if angle_c < 0 or angle_c >= 180:  # validates angle C is a positive & less than 180 degrees
            print("\nAngle C must be a positive number less than 180 degrees, please reenter:   ")
            angle_c = (float(input()))
        leg_c = math.sqrt(side_a * side_a + side_b * side_b - 2 * side_a * side_b *
                          math.cos(math.pi / 180 * angle_c))
        print("\nThe leg of the given triangle is ", format(leg_c, '.2f'), ".")
        break


def calculate_right_circular_cylinder():
    """This function calculates the volume of a Right Circular Cylinder"""
    while True:
        height = (float(input("\nPlease enter the height:    ")))
        if height < 0:  # validates if the height is a positive value
            print("\nThe height should be a positive number, please reenter:   ")
            height = (float(input()))
        radius = (float(input("\nPlease enter the radius:    ")))
        if radius < 0:  # validates if the radius is a positive value
            print("\nThe radius should be a positive number, please reenter:   ")
            radius = (float(input()))
        volume = math.pi * (radius * radius) * height  # calculation
        print("\nFor this Right Circular Cylinder the volume is ", format(volume, '.2f'))
        break


def main():
    """Runs the main program"""
    display_menu()  # displays menu options
    option = int(input())  # intakes user's option choice

    while option != 9:  # while loop for options that are not to exit.
        if option == 1:  # creates a password for the user
            password_generator()
        elif option == 2:  # gives the user a percentage value based on input
            calculate_percentage()
        elif option == 3:  # tells the user how many days from today until it will be July 4th, 2025
            days_until_july_4_2025()
        elif option == 4:  # calculates leg C of a triangle
            leg_of_triangle()
        elif option == 5:  # option to calculate the volume of a right circular cylinder
            calculate_right_circular_cylinder()
        else:
            print("This is an invalid option, please try again.")  # validates user's option choice
        print()
        display_menu()  # re-displays menu to user
        option = int(input("\nPlease enter your option:    "))

    print("\nThank you for using this program, now exiting... Good-bye!")


main()
