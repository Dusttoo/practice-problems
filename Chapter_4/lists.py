# Create a list of at least 3 kinds of pizza. Loop through the list.
# print a sentence for each pizza
# Add a statement outside of the loop

print('Exercsie 1:')
pizzas = ['Cheese', 'Pepperoni', 'Supreme']
for pizza in pizzas:
    print(f'I love {pizza} pizza!')
print('But really, I just love all pizza.')
print("-----------")

# Use a for loop to print the numbers 1-20 inclusive

print('Exercise 3:')
for number in range(1, 21):
    print(number)
print("-----------")

# Create a list of numbers from 1 - 1 million and then print each number
print('Exercise 4:')
numbers = [number for number in range(1, 1000001)]
# [print(number) for number in range(1, 1000001)]
# for nunmber in numbers:
#     print(number)
print("-----------")

# using the numbers above use min, max, and sum
print('Exercise 5:')
print(f' Min: {min(numbers)}\n Max: {max(numbers)}\n Sum: {sum(numbers)}')
print("-----------")

# Print a list of odd numbers
print('Exercise 6:')
[print(number) for number in range(1, 21, 2)]
print("-----------")

# Print a list of multiples of 3
print('Exercise 7:')
[print(number) for number in range(0, 31, 3)]
print("-----------")

# Print a list of the first 10 cubes
print('Exercise 8:')
[print(number**3) for number in range(1, 11)]
print("-----------")

# Use one of the lists above to slice the first 3 items, the middle 3 items, and the last 3 items.
print('Exercise 10:')
print(f'First 3: {numbers[:3]}, middle 3: {numbers[500000:500003]}, last 3: {numbers[-3:]}')
print("-----------")

# Make a copy of your pizza list called friends_pizza and add a new pizza to the original list, add a different one to the copy, prove that they are different.
print('Exercise 11:')
friends_pizza = pizzas[:]
pizzas.append('Pineapple')
friends_pizza.append('Buffalo Chicken')
print(f'My favorite pizzas are: ')
[print(pizza) for pizza in pizzas]
print(f'My friends favorite pizzas are: ')
[print(pizza) for pizza in friends_pizza]
