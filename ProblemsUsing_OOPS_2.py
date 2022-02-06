################################################################################################################
#
# 2. Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11
# Output : Odd Number
# Input : 8
# Output : Even Number

################################################################################################################

class Check:

	def __init__(self,a):
		self.iValue = a

	def ChckNum(self):
		sign = False

		if((self.iValue % 2) == 0):
			sign = True

		return sign	
			

def main():
	
	iNo = 0
	bRet = False

	print("Enter the Number :")
	iNo = int(input())

	cObj = Check(iNo)

	bRet = cObj.ChckNum()

	if(bRet == True):
		print("The Number is Even...")
	else:
		print("The Number is Odd...")	


if __name__ == '__main__':
			main()		