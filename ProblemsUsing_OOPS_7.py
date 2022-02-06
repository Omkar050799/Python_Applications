class Circle:

	def __init__(self):

		self.Radius = 0
		self.Area   = 0
		self.Circum = 0
		self.PI     = 3.14

	def Accept(self,R):
		self.Radius = R

	def CalculateArea(self):

		self.Area = self.PI * self.Radius * self.Radius; 

	def CalculateCircumference(self):	

		self.Circum =  2 * (self.Radius * self.PI)

	def Display(self):
		print("The radius of Circle : ",self.Radius)
		print("The Area of Circle : ",self.Area)
		print("The Circum ference of Circle : ",self.Circum)			


def main():

	obj = Circle()

	obj.Accept(15)
	obj.CalculateArea()
	obj.CalculateCircumference()
	obj.Display()


if __name__ == '__main__':
		main()	