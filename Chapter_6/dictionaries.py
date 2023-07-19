# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
print('Exercise 1:')
person = {
    'first_name': 'Michelle',
    'last_name': 'Mumphrey',
    'age': '39',
    'city': 'Gilmer'
}

print(person['first_name'], person['last_name'], person['age'], person['city'])

print("-----------")


# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
print('Exercise 2:')
favorite_numbers = {
    "Dusty": 7,
    "Michelle": 11,
    "Michael": 4,
    "Jenna": 2,
    "Bob": 6
}

for key, value in favorite_numbers.items():
    print(f'{key}\'s favorite number is {value}.')

print("-----------")


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character(\n)
print('Exercise 3:')
glossary = {
    "Loop": "Way to iterate through a collection",
    "Conditional": "Returns True or False value",
    "If": "Uses a conditional statement to perform an action",
    "Variable": "A placeholder for an object",
    "Dictionary": "A collection",
    "Python": "My favorite coding language",
    "String": "A collection of letters or numbers wrapped in \"\"",
    "Boolean": "True or False"
}
definition = glossary['Loop']
print(f'Loop: {definition}')
definition = glossary['Conditional']
print(f'Conditional: {definition}')
definition = glossary['If']
print(f'If: {definition}')
definition = glossary['Variable']
print(f'Variable: {definition}')
definition = glossary['Dictionary']
print(f'Dictionary: {definition}')


print("-----------")


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.
print('Exercise 4:')
for key, value in glossary.items():
    print(f'{key}: {value}')
print("-----------")


# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.
print('Exercise 5:')
rivers = {
    "nile": "egypt",
    "congo": "africa",
    "amazon": "south america"
}

for key, value in rivers.items():
    print(f'The {key} runs through {value}.')

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

print("-----------")


# 6-6. Polling: Use the code in favorite_languages.py(page 104).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not .
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
print('Exercise 6:')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
users = ['john', 'sarah', 'phylis', 'ferdenand', 'jen']

for user in users:
    if user in favorite_languages.keys():
        print(f'Thanks {user} for taking the poll!')
    else:
        print(f'{user} please take our poll.')

print("-----------")


# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
print('Exercise 7:')
person_2 = {
    'first_name': 'Dusty',
    'last_name': 'Mumphrey',
    'age': '26',
    'city': 'Gilmer'
}

person_3 = {
    'first_name': 'John',
    'last_name': 'Mumphrey',
    'age': '19',
    'city': 'Gilmer'
}

people = [person, person_2, person_3]

for user in people:
    print('Here is what I know about', user['first_name'])
    for key, value in user.items():
        print(f'{key}: {value}')


print("-----------")


# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
print('Exercise 8:')

print("-----------")


# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
print('Exercise 9:')

print("-----------")


# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.
print('Exercise 10:')

print("-----------")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in , its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.
print('Exercise 11:')

print("-----------")


# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.
print('Exercise 12:')

print("-----------")
