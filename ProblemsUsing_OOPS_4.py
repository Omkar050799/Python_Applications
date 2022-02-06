################################################################################################################
#
# Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1
################################################################################################################

class Check:

	def __init__(self,a):
		self.iValue = a

	def printName(self):

		for i in range(self.iValue,0,-1):
			print(i,end = " ")
		
			
def main():
	
	iNo = 0
	bRet = False

	print("Enter the Number to print Name that times :")
	iNo = int(input())

	cObj = Check(iNo)

	cObj.printName()

		

if __name__ == '__main__':
			main()		