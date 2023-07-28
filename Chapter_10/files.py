# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can.... Save the file as learning_python.txt in the
# same directory as your exercises from this chapter. Write a program that reads
# the file and prints what you wrote three times. Print the contents once by reading in the entire file, 
# once by looping over the file object, and once by storing
# the lines in a list and then working with them outside the with block.
print('Exercise 1:')
filename = 'learning_python.txt'
python_lines = []

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        python_lines.append(line)
        print(line.rstrip())

for line in python_lines:
    print(line.rstrip())

print("-----------")
# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word. Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >> > message = "I really like dogs."
# >> > message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.
print('Exercise 2:')

for line in python_lines:
    print(line.replace('Python', 'JavaScript').strip())


print("-----------")
# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
print('Exercise 3:')
print('Done')

# name = input('Welcome! Please enter your name > \n')

# with open('guests.txt', 'w') as guest_list:
#     guest_list.write(name)
# print(f'{name} successfully added to the guest list')

print("-----------")
# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.
from datetime import datetime
print('Exercise 4:')
print('Done')

# active = True
# message = f'Hello! Please enter your name > \n'
# message += f'Press \'q\' or \'quit\' to exit. \n'
# while active:
#     name = input(message)
#     if name == 'q' or name =='quit':
#         active = False
#     else:
#         current_time = datetime.now()
#         with open('guest_book.txt', 'a') as guest_book:
#             guest_book.write(f'{name} has visited at {datetime.date(current_time)} \n')
#         print(f'Thank you for visiting {name}! Your visit has been recorded. \n')




print("-----------")
# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.
print('Exercise 5:')
print('Done')

# active = True
# message = 'Why do you like programming?\n'
# message += f'Press \'q\' or \'quit\' to exit. \n'
# while active:
#     name = input("Welcome! What is your name? >\n")
#     if name.lower() == 'q' or name.lower() == 'quit':
#         active = False
#         break
#     reason = input(message)
#     if reason.lower() == 'q' or reason.lower() == 'quit':
#         active = False
#         break
#     with open('programming_reasons.txt', 'a') as programming_reasons:
#         programming_reasons.write(f'{name}: {reason}')

print("-----------")
# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.
print('Exercise 6:')
print('Done')

# active = True
# while active:
#     print('Hello! To exit press \'q\' or \'quit\' at any time.')
#     num_one = input("Please enter the first number to add: \n")
#     if num_one == 'q' or num_one == 'quit':
#         active = False
#         break

#     num_two = input("Please enter the second number to add: \n")
#     if num_two == 'q' or num_two == 'quit':
#         active = False
#         break

#     try:
#         print(f'{num_one} + {num_two} = {int(num_one) + int(num_two)}')
#     except ValueError:
#         print("Please enter a number.")



print("-----------")
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.
print('Exercise 7:')
print('Done')
print("-----------")
# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try -except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
# executes properly.
print('Exercise 8:')
files = ['cats.txt', 'birds.txt', 'dogs.txt']

for file in files:
    try:
        with open(file) as file_object:
            lines = file_object.readlines()
            file_title = file.split('.')[0]
            print(f'These are the {file_title} I know:')
            for line in lines:
                print(f'{line.rstrip()}')
            print('\n')
    except FileNotFoundError:
        print(f'Sorry, {file} does not exist. \n')

print("-----------")
# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.
print('Exercise 9:')
for file in files:
    try:
        with open(file) as file_object:
            lines = file_object.readlines()
            file_title = file.split('.')[0]
            print(f'These are the {file_title} I know:')
            for line in lines:
                print(f'{line.rstrip()}')
            print('\n')
    except FileNotFoundError:
        pass
print("-----------")
# 10-10. Common Words: Visit Project Gutenberg(http: // gutenberg.org /)
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >> > line = "Row, row, row your boat"
# >> > line.count('row')
# 2
# >> > line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for , regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.
print('Exercise 10:')
file_names = ['sherlock.txt', 'dracula.txt', 'alice.txt']
lines = ''
word_count = 0

for file in file_names:
    title = file.split('.')[0].title()
    try:
        with open(file) as book:
            lines = book.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            word_count += line.lower().count('the')
        print(f'The word \'the\' appears in {title} {word_count} times.')
        word_count = 0

print("-----------")
# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate program 
# that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”
import json
print('Exercise 11:')
# fav_number = input('What is your favorite number? \n')
# file_name = 'fav_number.json'
# with open(file_name, 'w') as file_obj:
#     json.dump(fav_number, file_obj)

# with open(file_name) as f_obj:
#     fav_number = json.load(f_obj)
#     print(f'Your favorite number is: {fav_number}')
print("Done")

print("-----------")
# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not , prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.
print('Exercise 12:')
file_name = 'fav_number.json'
try:
    with open(file_name) as f_obj:
        fav_number = json.load(f_obj)
except FileNotFoundError:
    fav_number = input('What is your favorite number? \n')
    with open(file_name, 'w') as file_obj:
        json.dump(fav_number, file_obj)
else:
    print(f'Your favorite number is: {fav_number}')

print("-----------")
# 10-13. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who
# last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not , call get_new_username() to get the correct
# username.
print('Exercise 13:')
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def remember_me():
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verify_user = input(f'Are you {username}? y/n\n')
        if verify_user.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            remember_me()

    else:
        remember_me()


greet_user()
print("-----------")
