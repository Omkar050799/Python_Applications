class Demo:
	value = 0

	def __init__(self,a,b):
		self.no1 = a
		self.no2 = b

	def fun(self):
	
		print("The value form Fun : ",self.no1)
		print("The value form Fun : ",self.no2)

	def Gun(self):
		print("The value form Gun : ",self.no1)
		print("The value form Gun : ",self.no2)	


def main():

	obj1 = Demo(11,21)
	obj2 = Demo(51,101)

	obj1.fun()
	obj2.fun()
	obj1.Gun()
	obj2.Gun()

if __name__ == '__main__':
		main()	