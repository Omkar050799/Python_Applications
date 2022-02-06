#5.Write a program which accept one number for user and check whether number is prime or not.
#Input :5
#Output : It is Prime Number
#
################################################################################

def ChkPrime(iNo):

	if((iNo%2) != 0):
		return True
	else:
		return False	
			

def main():
	iValue = 0
	bRet = False

	print("Enter the Number : ")
	iValue = int(input())

	bRet = ChkPrime(iValue)
	
	if(bRet == True):
		print("The Number is Prime")
	else:
		print("The Number is Not Prime")
		
   
if __name__ == '__main__':
	main()