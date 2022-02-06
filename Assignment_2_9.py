#9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934
#Output : 7
#
################################################################################

def ChkLength(iNo):
	return len(iNo)
	
	

def main():
	iValue = 0

	print("Enter the Row")
	iValue = (input())

	iRet = ChkLength(iValue)

	print(iRet)


if __name__ == '__main__':
	main()