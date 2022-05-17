# It should have 9 digits.
# It should be divided into 3 parts by hyphen (-).
# The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
# The second part should have 2 digits and it should be from 01 to 99.
# The third part should have 4 digits and it should be from 0001 to 9999.

def string_validation(s):
    if s.count('-') != 2:
        return  False
    s = s.replace('-')
    if s.isnumeric() and len(s) != 9:
        return False

    return True

def check(n):

    if len(n[0]) != 2 or len(n[1]) != 2 or len(n[2]) != 4:  # Check every part's length
        return False
    elif int(n[0]) == 0 or int(n[1]) == 0 or int(n[2]) == 0:  # Checks if any part is 0
        return False
    elif int(n[0]) > 900 or n[0] == '666':  # Checks additional rules for 1st part
        return False
    else:
        return True


def main():
    print("Welcome to the Social Security Number Validator")

    SSN = input("Enter the Social Security Number Validator")
    if string_validation(SSN):
        # s = SSN.split('-')
        if check(SSN.split('-')):
            print("The Social Security Number is valid!!")
        else:
            print("The Social Security Number is invalid")
