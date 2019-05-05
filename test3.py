import math

class User(object):
	"""
	Attribute
		name String
		price int
		year int
		groceries bool
	"""
	def __init__(self, name, price, year, groceries):
		self.name = name
		self.price = price
		self.year = year
		self.groceries = groceries

	def getDiscount(self):
		if self.groceries is not True:
			if(self.name == "Employee"):
				return self.price - (self.price * 0.3)
			elif(self.name == "Affiliate"):
				return self.price - (self.price * 0.1)
			else:
				if(self.year >= 2):
					return self.price - (self.price * 0.05)
				else:
					mod = self.price / 100
					discount = math.floor(mod) * 5
					return self.price - discount
		else:
			return self.price

def main():
	user = raw_input("input 'Employee / Affiliate / Customer': ")

	price = input("input price: ")
	groceries = raw_input("input groceries [y/n]: ")
	year = raw_input("input year user: ")
	t_groceries = False;
	if(groceries == "y"):
		t_groceries = True
	result = User(user, price, year, t_groceries)
	bill = result.getDiscount()
	print(bill)

if __name__ == '__main__':
	main()
