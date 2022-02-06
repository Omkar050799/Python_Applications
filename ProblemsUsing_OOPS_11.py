class Number:

	def __init__(self,a):
		self.Value = a
		print("Number : ",self.Value)

	def ChkPrime(self):

		for i in range(2,self.Value,1):
			if((self.Value % i) == 0):
				break

		i = i + 1		

		if i == self.Value:
			print("The Number is Prime...")
		else:
			print("The Number is Not Prime...")			



	def ChkPerfect(self):

		Number = self.Value
		iFact = 0

		for i in range(1,self.Value):
			if ((self.Value % i) == 0):
				iFact = iFact + i
			
		if(iFact == Number):
			print("Yes Its A Perfect Number...")
		else:
			print("Its Not a Perfect Number...")

	def Factors(self):

		print("Factors of Given Number are : ")

		for i in range(1,self.Value):
			if ((self.Value % i) == 0):
				print(i)			

	
	def SumFactors(self):
		iFact = 0

		for i in range(1,self.Value):
			if ((self.Value % i) == 0):
				iFact = iFact + i
			
		print("Sum of Factors : ",iFact)

	
			


def main():

	obj1 = Number(6)

	obj1.ChkPrime()
	obj1.Factors()
	obj1.ChkPerfect()
	obj1.SumFactors()




if __name__ == '__main__':
		main()	