import unittest
from city_functions import geo_concat3

class Test_geo_concat(unittest.TestCase) :

	def test_city_country (self) :
		result = geo_concat3("New York", "United States")
		self.assertEqual(result,"New York, United States")
		result = geo_concat3("London", "England")
		self.assertEqual(result,"London, England")
		result = geo_concat3("Paris", "France")
		self.assertEqual(result,"Paris, France")

	def test_city_country_population (self) :
		result = geo_concat3("Anchorage", "United States", 288000)
		self.assertEqual(result,"Anchorage, United States - population 288,000")

unittest.main()
