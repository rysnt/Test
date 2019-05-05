import unittest
import random
import math 

class TestBill(unittest.TestCase):
	def test_employee(self):
		"""
		Test payment employee with price 1000 multiply discount 
		"""
		price = 1000
		result = price - (price * 0.3)
		self.assertEqual(result, 700)

	def test_affiliate(self):
		"""
		Test payment affiliate with price 1000 multiply discount
		"""
		price = 1000
		result = price - (price * 0.1)
		self.assertEqual(result, 900)

	def test_customer(self):
		"""
		Test payment customer with price 1000 and year more than 2
		"""
		price = 1000
		result = price - (price * 0.05)
		self.assertEqual(result, 950)

	def test_newcustomer(self):
		"""
		Test payment customer with price 1000 and less than 2
		"""
		price = 1000
		mod = price / 100
		result = price - (math.floor(mod) * 5)
		self.assertEqual(result, 950)


if __name__ == '__main__':
	unittest.main()