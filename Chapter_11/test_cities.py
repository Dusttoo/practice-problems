# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to test).
# Write a method called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run
# test_cities.py, and make sure test_city_country() passes.
import unittest
from city_functions import name_city, name_city_with_pop
print('Exercise 1:')
class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does the city and country return successfully"""
        city_name = name_city('santiago', 'chile')
        self.assertEqual(city_name, 'Santiago, Chile')

# 11-2. Population: Modify your function so it requires a third parameter,
# population. It should now return a single string of the form City, Country –
# population xxx, such as Santiago, Chile – population 5000000. Run
# test_cities.py again. Make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run
# test_cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies you 
# can call your function with the values 'santiago', 'chile', and
# 'population=5000000'. Run test_cities.py again, and make sure this new test
# passes.
    def test_city_with_no_pop(self):
        city_name = name_city_with_pop('santiago', 'chile')
        self.assertEqual(city_name, 'Santiago, Chile')

    def test_city_with_pop(self):
        city_name = name_city_with_pop('santiago', 'chile', 50000)
        self.assertEqual(city_name, 'Santiago, Chile - 50000')

unittest.main()

print("-----------")
