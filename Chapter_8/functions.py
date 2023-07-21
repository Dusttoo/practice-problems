# 8-1. Message: Write a function called display_message() that prints one sentence telling 
# everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
print('Exercise 1:')
def display_message():
    print('I am learning about functions!')
display_message()
print("-----------")
# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
print('Exercise 2:')
def favorite_book(title):
    print(f'One of my favorite books is {title.title()}')

favorite_book('where the red fern grows')
print("-----------")
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
print('Exercise 3:')


def make_shirt(message='I love Python', size='large'):
    print(f'Your shirt is size {size} and says {message}.')

make_shirt('Hello', 'small')
make_shirt(size='medium', message='Hello')
print("-----------")
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
print('Exercise 4:')
make_shirt(size='medium')
make_shirt()
make_shirt('Hello', 'small')

print("-----------")
# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country
print('Exercise 5:')
def describe_city(city, country='United States'):
    print(f'{city} is in {country}')
describe_city('Seattle')
describe_city('Venice', 'Italy')
describe_city('Austin')
print("-----------")
# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.
print('Exercise 6:')
def city_country(city, country):
    print(f'{city}, {country}')
city_country('Seattle', 'Washington')
city_country('Austin', 'Texas')
city_country('Portland', 'Oregon')

print("-----------")
# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.
print('Exercise 7:')
def make_album(artist, title, num_tracks=0):
    if not num_tracks:
        return {'artist': artist, 'title': title}
    else:
        return {'artist': artist, 'title': title, 'num_tracks': num_tracks}

the_weeknd = make_album('The Weeknd', 'Beauty Behind The Madness')
drake = make_album('Drake', 'Take Care', 18)
nicki_minaj = make_album('Nicki Minaj', 'The Pink Print')
print(the_weeknd)
print(drake)
print(nicki_minaj)


print("-----------")
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
print('Exercise 8:')
# active = True

# while active:
#     print(f'Enter \'q\' to quit.')
#     album_name = input("Enter an album > ")
#     if album_name == 'q':
#         break

#     artist = input("Enter an artist > ")
#     if artist == 'q':
#         break

#     album = make_album(artist, album_name)
#     print(f'Here is your album: {album}')

print("-----------")
# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.
print('Exercise 9:')
magicians = ['Peter', 'Paul', 'Mary', 'Sue']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)

print("-----------")
# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding 
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
print('Exercise 10:')
def make_great(magicians):
    length = len(magicians)
    for i in range(length):
        magician = magicians.pop(0)
        magicians.append(f'Great {magician}')
        i += 1
# make_great(magicians)
# show_magicians(magicians)
    
print("-----------")
# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.
print('Exercise 11:')
magicians_copy = magicians[:]

make_great(magicians_copy)
show_magicians(magicians)
show_magicians(magicians_copy)

print("-----------")
# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich 
# that is being ordered. Call the function three times, using a different number of arguments each time.
print('Exercise 12:')
def create_sandwich(*sandwich_items):
    response = 'Your sandwich will have '
    if len(sandwich_items) == 1:
        response += f'{sandwich_items[0]}.'
        return response

    for item in sandwich_items:
        if item == sandwich_items[-1]:
            response += f'and {item}.'
        else:
            response += f'{item}, '
    return response

print(create_sandwich('Lettuce', 'Tomatoes', 'Pickles', 'Ham'))
print(create_sandwich('Ham'))
print(create_sandwich('Turkey', 'Cheese'))

print("-----------")
# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.
print('Exercise 13:')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('dusty', 'mumphrey',
                             favorite_color='blue',
                             height='5\'3',
                             favorite_book='Where the red fern grows')
print(user_profile)

print("-----------")
# 8-14. Cars: Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.
print('Exercise 14:')
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

print("-----------")
# 8-15. Printing Models: Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions.
print('Exercise 15:')
from printing_models import print_models, show_completed_models
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("-----------")
# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
print('Exercise 16:')

print("-----------")
# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.
print('Exercise 17:')

print("-----------")
