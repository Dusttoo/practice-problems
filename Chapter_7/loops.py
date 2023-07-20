# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
print('Exercise 1:')
# car = input("What kind of rental would you like? ")
# print(f'Let me see if I can find you a {car}')
print("-----------")


# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, 
# print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
print('Exercise 2:')
# num_people = input("How many people are in your party? ")
# if int(num_people) > 8:
#     print(f'You will have to wait a little longer.')
# else:
#     print('Your table is ready.')
print("-----------")


# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not .
print('Exercise 3:')
# num = input("Pick a number ")
# if int(num) % 10 == 0:
#     print(f'{int(num)} is a multiple of 10.')
# else:
#     print(f'{int(num)} is not a multiple of 10.')
print("-----------")


# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
print('Exercise 4:')
# prompt = "\nEnter the toppings you would like to add."
# prompt += "\nWhen you are finished enter 'quit'\n"
# topping = ''
# while topping != 'quit':
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f'I will add {topping} to your pizza.')

print("-----------")


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free
# if they are
# between 3 and 12, the ticket is $10
# and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
print('Exercise 5:')
# prompt = '\nEnter your age: '
# name = input("What is your name? > ")

# age = ''

# while age != 'quit':
#     age = input(prompt)
#     if age != 'quit':
#         if int(age) < 3:
#             print(f'{name} your ticket is free.')
#         elif int(age) < 13:
#             print(f'{name} your ticket is $10.')
#         else:
#             print(f'{name} your ticket is $15.')
#     else:
#         print(f'Thank you {name}, come again.')

print("-----------")


# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value.
print('Exercise 6:')
prompt = "\nEnter the toppings you would like to add."
prompt += "\nWhen you are finished enter 'quit'\n"
topping = ''
active = True

# while active:
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f'I will add {topping} to your pizza.')
#     else:
#         active = False

# while topping != 'quit':
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f'I will add {topping} to your pizza.')

# while topping != 'quit':
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f'I will add {topping} to your pizza.')
#     else:
#         break

print("-----------")


# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)
print('Exercise 7:')
# active = True

# while active:
#     print("Oops")

print("-----------")


# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
print('Exercise 8:')
sandwich_orders = ['Rueben', 'Club', 'Monte Cristo', 'Club']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f'I made your {finished_sandwich} sandwich.')
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f'The {sandwich} sandwich is complete.')

print("-----------")


# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
print('Exercise 9:')
sandwich_orders = ['Rueben', 'Pastrami',
                   'Club', 'Monte Cristo', 'Club', 'Pastrami', 'Pastrami']
print('Sandwiches to be made today: ')
for sandwich in sandwich_orders:
    print(sandwich)
print(f'The deli has run out of Pastrami.')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print('Processing orders: ')
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f'I made your {finished_sandwich} sandwich.')
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f'The {sandwich} sandwich is complete.')


print("-----------")


# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.
print('Exercise 10:')
prompt = 'Welcome to my poll.\n'
prompt += 'What is your name?\n'
active = True

results = {}

while active:
    name = input(prompt)
    location = input('If you could visit anywhere in the world, where would it be? \n')
    results[name] = location
    proceed = input('Ask another person? y/n\n')

    if proceed == 'n':
        active = False
        print('Thanks for participating. Here are the results of the poll:')
        for key, value in results.items():
            print(f'{key} would like to visit {value}.')




print("-----------")
