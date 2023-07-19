# Store the names of a few friends in a list called names.
# Print each person's name one at a time

print('Exercise 1:')
names = ['Michelle', 'Olyvia', 'Christina']
print(names[0])
print(names[1])
print(names[2])
print("-----------")
# Use the same list to print a personalized message to each friend

print('Exercise 2:')
print(f'Hello, {names[0]}. How are you?')
print(f'Hello, {names[1]}. How are you?')
print(f'Hello, {names[2]}. How are you?')
print("-----------")

# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list and then use that list to print a message to each person

print('Exercise 4:')
guests = ['Barrack Obama', 'Michelle Mumphrey', 'Terry Mumphrey', 'Kristen Harper']
print(f'Dear {guests[0]}, you are invited')
print(f'Dear {guests[1]}, you are invited')
print(f'Dear {guests[2]}, you are invited')
print(f'Dear {guests[3]}, you are invited')

print(f'{guests[2]} can not make it')
print("-----------")

# Modify the above list to replace the guest who can not make it with the new guest to invite
print('Exercise 5:')
del guests[2]
guests.insert(2, 'Black Panther')
print(f'Dear {guests[0]}, you are invited')
print(f'Dear {guests[1]}, you are invited')
print(f'Dear {guests[2]}, you are invited')
print(f'Dear {guests[3]}, you are invited')
print(f'We found a bigger table!')
print("-----------")

# Modify the above list to add 3 new guests. 1 in front, in middle, and at end
print('Exercise 6:')
guests.insert(0, 'Yenko')
guests.insert(2, 'Toast')
guests.append('Aspen')
print(f'Dear {guests[0]}, you are invited')
print(f'Dear {guests[1]}, you are invited')
print(f'Dear {guests[2]}, you are invited')
print(f'Dear {guests[3]}, you are invited')
print(f'Dear {guests[4]}, you are invited')
print(f'Dear {guests[5]}, you are invited')
print(f'Dear {guests[6]}, you are invited')
print("-----------")

# Remove everyone from your list one at a time
# Pop everyone but two and print a message uninviting them
# delete the final 2 guests and print the empty list
print('Exercise 6:')
popped_guest = guests.pop()
print(f'Sorry {popped_guest}, there is not enough room anymore.')
popped_guest = guests.pop()
print(f'Sorry {popped_guest}, there is not enough room anymore.')
popped_guest = guests.pop()
print(f'Sorry {popped_guest}, there is not enough room anymore.')
popped_guest = guests.pop()
print(f'Sorry {popped_guest}, there is not enough room anymore.')
popped_guest = guests.pop()
print(f'Sorry {popped_guest}, there is not enough room anymore.')
print(f'{guests[0]}, you are still invited.')
print(f'{guests[1]}, you are still invited.')
del guests[0]
del guests[0]
print(f'Final list: {guests}')
print("-----------")

# Think of 5 places in the world you would like to visit. Store the locations in a list.
# Print the list in it's original order
# Use sorted() to print in alphabetical order without modifying the original
# Print the list in the original order
# Use reverse to change the order
# Use reverse again
# Use sort to sort in alphabetical order
# Use sort to sort in reverse alphabetical order

print('Exercise 8:')
places_to_visit = ['Venice', 'Seattle', 'Portland', 'Alaska', 'Mexico']
print(places_to_visit)
print(f'Sorted: {sorted(places_to_visit)}')
print(places_to_visit)
places_to_visit.reverse()
print(f'Reversed: {places_to_visit}')
places_to_visit.reverse()
print(f'Reversed again: {places_to_visit}')
places_to_visit.sort()
print(f'Sort: {places_to_visit}')
places_to_visit.sort(reverse=True)
print(f'Sorted reverse: {places_to_visit}')
print("-----------")

# Print the length of one of the guest lists above

print('Exercise 9: ')
print(f'I invited {len(names)} people to my party.')
print("-----------")

# Write a list and use every function in this chapter at least once.
my_list = ['Zebra', 'Cow', 'Duck', 'Dog', 'Cat', 'Tiger']
print(f'I know {len(my_list)} animals. The {my_list[2]} is my favorite animal. I currently know these animals: {my_list}')
my_list.insert(2, 'Fish')
my_list.append('Bear')
print(f'Today I learned about the {my_list[2]} and {my_list[-1]}. Now I know these animals: {my_list}')
my_list.sort()
popped_item = my_list.pop()
print(f'Today I forgot what a {popped_item} is. I now only know these animals: {my_list}')
my_list.sort(reverse=True)
del my_list[3]
print(f'These are the animals I now know: {my_list}')
