################################################################################################################
#
# 6.Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11
# Output : Positive Number
# Input : -8
# Output : Negative Number
# Input : 0
# Output : Zero
################################################################################################################

class NumberX:

	def __init__(self,a):
		self.iNo = a

	def CheckNum(self):
		if(self.iNo < 0):
			return 11
		elif(self.iNo > 0):
			return 12
		else:
			return 13			

def main():

	iNo = 0
	iRet = 0

	iNo = int(input("Enter the Number : "))

	nObj = NumberX(iNo)

	iRet = nObj.CheckNum()

	if(iRet == 11):
		print("The Number is Negative Number")
	elif(iRet == 12):
		print("The Number is Positive Number")
	else:
		print("The Number is 0")	


if __name__ == '__main__':
	main()