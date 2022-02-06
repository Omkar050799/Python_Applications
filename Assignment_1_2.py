def ChkNum(iValue):
    
	if((iValue % 2) == 0):
		return True
	else:
	    return False	

def main():
	iNo = 0
	bRet = False

	print("Enter Number : ")
	iNo = int(input())

	bRet = ChkNum(iNo)

	if(bRet == True):
		print("The Number is Even...")
	else:
	    print("The Number is Odd...c")	

if __name__ == '__main__':
	main()	