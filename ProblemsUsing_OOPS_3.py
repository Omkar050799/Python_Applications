################################################################################################################
#
# Write a program which display 5 times Marvellous on screen.
# Output :
# Marvellous
# Marvellous
# Marvellous
# Marvellous
# Marvellous

################################################################################################################

class Check:

	def __init__(self,a):
		self.iValue = a

	def printName(self):

		for i in range(self.iValue):
			print("Marvellous...")
		
			
def main():
	
	iNo = 0
	bRet = False

	print("Enter the Number to print Name that times :")
	iNo = int(input())

	cObj = Check(iNo)

	cObj.printName()

		

if __name__ == '__main__':
			main()		