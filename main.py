import random

NUMBERS = '0123456789'
SPECIAL = '!@#$%^&*()_+'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'

def generate_password(num_chars, include_special, include_nums, include_upper, include_lower):
    all_chars = ''
    password = ''

    if include_special == 'y':
        all_chars += SPECIAL
    if include_nums == 'y':  
        all_chars += NUMBERS
    if include_upper == 'y':
        all_chars += UPPER
    if include_lower == 'y':
        all_chars += LOWER

    # Generate the password
    for i in range(int(num_chars)):
        password += random.choice(all_chars)

    print('Your password is: ' + password)

def tests_user_input(prompt):
    # Test the user input
    user_input = input(prompt).strip().lower()
    while user_input != 'y' and user_input != 'n':
        print('Invalid input. Please enter either "y" or "n".')
        user_input = input(prompt)
    return user_input

# This program generates a password based on the user's input
print('Welcome to the password generator! Please enter the fields below to generate a password.\n')
do_again = 'y'

while do_again == 'y':
    # Prompt the user for an amount of characters
    num_chars = input('Enter the amount of characters: ')
    while not num_chars.isdigit():
        print('Invalid input. Please enter a number.')
        num_chars = input('Enter the amount of characters: ')

    # Ask the user if they would like to include special characters
    include_special = tests_user_input('Would you like to include special characters? (y/n): ')

    # Ask the user if they would like to include numbers
    include_nums = tests_user_input('Would you like to include numbers? (y/n): ')

    # Ask the user if they would like to include uppercase letters
    include_upper = tests_user_input('Would you like to include uppercase letters? (y/n): ')

    # Ask the user if they would like to include lowercase letters
    include_lower = tests_user_input('Would you like to include lowercase letters? (y/n): ')

    print()
    
    generate_password(num_chars, include_special, include_nums, include_upper, include_lower)

    do_again = tests_user_input('Would you like to generate another password? (y/n): ')

print('Thank you for using the password generator!')

