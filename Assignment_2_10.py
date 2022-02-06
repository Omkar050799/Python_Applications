#9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934
#Output : 7
#
################################################################################

def CountSumDigit(iNo):
	iSum = 0
	iDigit = 0


	while iNo > 0:
		iDigit = iNo % 10
		iSum = int(iSum) + int(iDigit)
		iNo = iNo/10
	
	return iSum

def main():
	iValue = 0

	print("Enter the Number")
	iValue = int(input())

	iRet = CountSumDigit(iValue)

	print(iRet)


if __name__ == '__main__':
	main()