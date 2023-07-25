from restaurant import Restaurant, IceCreamStand

new_restuaraunt = Restaurant('Dustys', 'American')
new_restuaraunt.describe_restaurant()
message = f'{new_restuaraunt.restaurant_name} has served {new_restuaraunt.number_served}'
print(message)
new_restuaraunt.set_number_served(5)
new_restuaraunt.increment_number_served(20)

my_stand = IceCreamStand('Bahama Bucks', 'Ice Cream', [
                         'chocolate', 'vanilla', 'rocky road', 'strawberry'])
my_stand.display_flavors()
