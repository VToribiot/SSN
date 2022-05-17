import os


def string_validation(s):
    if s.count('-') != 2:  # Checks the number of hyphens that needs to have the SSN
        return False
    s = s.replace('-', '')
    if not s.isnumeric() or len(s) != 9:  # Checks the SSN has 9 digits
        return False

    return True


def check(n):

    if len(n[0]) != 3 or len(n[1]) != 2 or len(n[2]) != 4:  # Check every part's length
        return False
    elif int(n[0]) == 0 or int(n[1]) == 0 or int(n[2]) == 0:  # Checks if any part is 0
        return False
    elif int(n[0]) > 900 or n[0] == '666':  # Checks additional rules for 1st part
        return False
    else:
        return True


def main():
    print("Welcome to the Social Security Number Validator")

    control = True
    while control:
        while True:
            ssn = input("\nEnter the Social Security Number Validator: ")  # Asks for the SSN
            if string_validation(ssn): # Invokes the input validation function
                break
            else:
                print("You entered an invalid input, please try again")

        if check(ssn.split('-')):  # Invokes the SSN Validator Function
            print("\nThe Social Security Number is valid!!")
        else:
            print("\nThe Social Security Number is invalid")

        while True:
            question = input("\nDo you want to leave the program (y/n): ")
            if question.lower() == 'y':
                os.system('cls')
                print("Thank you for using the program!!")
                control = False
                break
            elif question.lower() != 'y' and question.lower() != 'n':
                print("You entered an invalid option, please try again")
            else:
                os.system('cls')
                break

main()