def ChkDiv(iNo):
	if((iNo % 5) == 0):
		return True
	else:
		return False	

def main():
	iValue = 0
	bRet = False

	print("Enter the Value to Check : ")
	iValue = int(input())

	bRet = ChkDiv(iValue)

	if(bRet == True):
		print(iValue, " is Divisible by 5")
	else:
		print(iValue, " is Not Divisible by 5")	



if __name__ == '__main__':
	main()