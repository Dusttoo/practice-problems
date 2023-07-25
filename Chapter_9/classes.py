# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating 
# that the restaurant is open.
# Make an instance called restaurant from your class . 
# Print the two attributes individually, and then call both methods.
print('Exercise 1:')
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    
    def describe_restaurant(self):
        print(f'This restaurant is called {self.restaurant_name.title()} and serves {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open.')
    
    def set_number_served(self, num_served):
        self.number_served = num_served
        print(f'{self.restaurant_name} has served {self.number_served}')
    
    def increment_number_served(self, num_served):
        self.number_served += num_served
        print(f'{self.restaurant_name} has served {self.number_served}')

restaurant = Restaurant("Torchys", "Mexican")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("-----------")
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class , and call describe_restaurant() for each
# instance.
print('Exercise 2:')
cheddars = Restaurant('Cheddars', 'American')
chuys = Restaurant('Chuys', 'Tex-Mex')
canes = Restaurant('Raising Canes', 'American')

cheddars.describe_restaurant()
chuys.describe_restaurant()
canes.describe_restaurant()

print("-----------")
# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
print('Exercise 3:')
class User():
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        pronoun = 'She' if self.gender.lower() == 'female' else 'He'
        print(f'Meet {self.first_name.title()} {self.last_name.title()}. {pronoun} is {str(self.age)} years old and live in {self.location.title()}.')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'{self.first_name.title()} has {self.login_attempts} login attempts.')
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Login attempts reset. {self.first_name.title()} has {self.login_attempts} login attempts.')


dusty = User('dusty', 'mumphrey', 27, 'male', 'gilmer')
michelle = User('michelle', 'mumphrey', 39, 'female', 'gilmer')
bob = User('bob', 'smith', 54, 'male', 'texarkana')

dusty.describe_user()
michelle.describe_user()
bob.describe_user()

print("-----------")
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class . Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number you 
# like that could represent how many customers were served in, say, a
# day of business.
print('Exercise 4:')
new_restuaraunt = Restaurant('Dustys', 'American')
new_restuaraunt.describe_restaurant()
message = f'{new_restuaraunt.restaurant_name} has served {new_restuaraunt.number_served}'
print(message)
new_restuaraunt.set_number_served(5)
new_restuaraunt.increment_number_served(20)

print("-----------")
# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_login_attempts() 
# that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
print('Exercise 5:')
new_user = User('dusty', 'mumphrey', 27, 'male', 'gilmer')
print(f'{new_user.first_name.title()} has {new_user.login_attempts} login attempts.')
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.reset_login_attempts()



print("-----------")
# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work
# just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.
print('Exercise 6:')

print("-----------")
# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.
print('Exercise 7:')

print("-----------")
# 9-8. Privileges: Write a separate Privileges class . The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class . Make a Privileges instance
# as an attribute in the Admin class . Create a new instance of Admin and use your
# method to show its privileges.
print('Exercise 8:')

print("-----------")
# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.
print('Exercise 9:')

print("-----------")
# 9-10. Imported Restaurant: Using your latest Restaurant class , store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is working properly.
print('Exercise 10:')

print("-----------")
# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.
print('Exercise 11:')

print("-----------")
# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.
print('Exercise 12:')

print("-----------")
# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.
print('Exercise 13:')

print("-----------")
# 9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
print('Exercise 14:')

print("-----------")
# 9-15. Python Module of the Week: One excellent resource for exploring the
# Python standard library is a site called Python Module of the Week. Go to
# http: // pymotw.com / and look at the table of contents. Find a module that
# looks interesting to you and read about it,
print('Exercise 15:')

print("-----------")
