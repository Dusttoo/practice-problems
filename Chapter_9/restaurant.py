class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f'This restaurant is called {self.restaurant_name.title()} and serves {self.cuisine_type} cuisine.')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is now open.')

    def set_number_served(self, num_served):
        self.number_served = num_served
        print(f'{self.restaurant_name} has served {self.number_served}')

    def increment_number_served(self, num_served):
        self.number_served += num_served
        print(f'{self.restaurant_name} has served {self.number_served}')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        flavors = 'This stand has '
        for flavor in self.flavors:
            if flavor != self.flavors[-1]:
                flavors += f'{flavor}, '
            else:
                flavors += f'and {flavor}.'
        print(flavors)
