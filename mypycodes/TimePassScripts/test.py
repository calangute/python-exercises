def name_deco(name):
	def deco(func):
		def wrapper(*args, **kwargs):
			return "Balance of {0}: Rs.{1}" .format(name,func(*args, **kwargs))
		return wrapper
	return deco

class cust_reg(object):
	'''bla bla car bla bla car bla bla car'''
	def __init__(self,name,initial):
		self.name=name
		self.balance=initial
	def withdraw(self,amount):
		self.balance-=amount
	def deposit(self,amount):
		self.balance+=amount
	@name_deco('name')
	def show(self):
		return (self.balance)
	
		


cust1 = cust_reg("Mani",1000)
cust2 = cust_reg("Deepak",2500)

cust1.withdraw(230)
cust2.deposit(170)

print cust2.show()
print cust1.show()