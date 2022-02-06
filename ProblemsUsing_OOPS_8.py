class Arithemtic:

	def __init__(self,A,B):
		self.Value1 = A
		self.Value2 = B

	def Addiition(self):
		Ans = 0
		Ans = self.Value1 + self.Value2

		print("Addition is : ",Ans)

	def Substraction(self):
		
		Ans = 0
		Ans = self.Value1 - self.Value2
		print("Substraction is : ",Ans)
	
	def Multiplication(self):
		
		Ans = 0.0
		Ans = self.Value1 * self.Value2
		print("Multiplication is : ",Ans)

	def Division(self):
		
		Ans = 0.0	
		Ans = self.Value1 / self.Value2
		print("Division is : ",Ans)


def main():

	obj = Arithemtic(10,10)

	obj.Addiition() 
	obj.Substraction()
	obj.Multiplication()
	obj.Division()

if __name__ == "__main__":
	main()	