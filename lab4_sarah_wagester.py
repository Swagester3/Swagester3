"""Sarah Wagester
SDEV 300 6981
This program validates a phone number and zip code.
Then it performs matrix operations requested."""

import sys
import re
import numpy as np


def validate_pattern(input_string, pattern, error_message):
    """Function to validate input against a pattern"""
    if not re.fullmatch(pattern, input_string):
        print(error_message)
        return False
    return True


def valid_length(input_string, length, error_message):
    """Function to verify the length of an input string"""
    if len(input_string) != length:
        print(error_message)
        return False
    return True


def validate_phone_pattern(number):
    """Function to validate phone number input"""
    pattern = r"\d{3}-\d{3}-\d{4}"  # pattern of 3 numbers, a dash, 3 numbers a dash & 4 more nums
    error_message = "This number is not in the correct format, please retry."
    return validate_pattern(number, pattern, error_message)


def validate_zip_pattern(zip_code):
    """Function to validate zip code input"""
    pattern = r"\d{5}-\d{4}"  # pattern of 5 numbers followed by a dash and 4 more numbers
    error_message = "This zipcode does not fit the xxxxx-xxxx format, please try again."
    return validate_pattern(zip_code, pattern, error_message)


def display_operation_menu():
    """Displays operation choice to user"""
    print("\nSelect a Matrix Operation from the list below: ")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")


def perform_operations(input_matrix, other_input_matrix, operation):
    """Function to perform operations"""
    if operation == 'a':
        operation_name = 'Addition'
        operation_matrix = input_matrix + other_input_matrix  # performs calculation
    elif operation == 'b':
        operation_name = 'subtraction'
        operation_matrix = input_matrix - other_input_matrix  # performs calculation
    elif operation == 'c':
        operation_name = 'multiplication'
        operation_matrix = np.matmul(input_matrix, other_input_matrix)  # performs calculation
    elif operation == 'd':
        operation_name = "element by element multiplication"
        operation_matrix = np.multiply(input_matrix, other_input_matrix)  # performs calculation
    else:
        print("This is an invalid option, please try again.")
        return
    print(f"\nYou selected {operation_name}. The results are:")  # print results
    np.savetxt(sys.stdout, operation_matrix, fmt='%g')

    print("\nThe Transpose is:")
    transpose_result = operation_matrix.transpose()  # performs transposing
    np.savetxt(sys.stdout, transpose_result, fmt='%g')

    print("\nThe row and column mean values of the results are:")
    row_mean = ', '.join(f"{mean:.2f}" for mean in operation_matrix.mean(axis=1))
    column_mean = ". ".join(f"{mean:.2f}" for mean in operation_matrix.mean(axis=0))
    print("Row: ", row_mean)  # prints means of the rows
    print("Column: ", column_mean)  # prints means of the column


def main():
    """Runs the main program"""
    print("\n********* Welcome to the Python Matrix Game! *********")
    while True:
        print("\nDo you want to play the Matrix Game?\n")
        option = input("Enter Y for Yes or N for No: ")  # intakes user's option to continue
        if option != 'Y':
            print("\nThank you for using this program, now exiting... Good-bye!")
            return

        while True:  # validates phone number
            number = input("\nEnter your phone number in the following format (xxx-xxx-xxxx): ")
            if validate_phone_pattern(number) and valid_length(number, 12, "This phone number "
                                                            "is not long enough, please try again"):
                break

        while True:  # validates zipcode
            zip_code = input("\nPlease enter your zip code+4 (xxxxx-xxxx): ")
            if validate_zip_pattern(zip_code) and valid_length(zip_code, 10, "This zip code is not "
                                                                "long enough, please try again"):
                break

        while True:  # verifies 1st matrix
            print("\nEnter your first 3x3 matrix:")
            try:
                first_matrix = [list(map(float, input().split())) for _ in range(3)]
                if len(first_matrix) != 3 or any(len(row) != 3 for row in first_matrix):
                    raise ValueError("This matrix should have 3 rows and 3 columns.")
            except ValueError:
                print("\nThe value must be a float or integer, please retry.")
                continue

            print("\nYour first 3x3 matrix is:")
            input_matrix = np.array(first_matrix).reshape(3, 3)
            np.savetxt(sys.stdout, input_matrix, fmt='%g')
            break

        while True:  # verifies 1st matrix
            print("\nEnter your second 3x3 matrix:")
            try:
                second_matrix = [list(map(float, input().split())) for _ in range(3)]
                if len(second_matrix) != 3 or any(len(row) != 3 for row in second_matrix):
                    raise ValueError("This matrix should have 3 rows and 3 columns.")
            except ValueError:
                print("\nThe value must be a float or integer, please retry.")
                continue
            print("\nYour second 3x3 matrix is:")
            other_input_matrix = np.array(second_matrix).reshape(3, 3)
            np.savetxt(sys.stdout, other_input_matrix, fmt='%g')
            break

        display_operation_menu()
        operation = input()

        perform_operations(input_matrix, other_input_matrix, operation)

        print("\n******* Thanks for playing Python Numpy *******")


main()
