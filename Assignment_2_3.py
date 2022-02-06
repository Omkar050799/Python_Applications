#3. Write a program which accept one number from user and return its factorial.
#Input :5
#Output : 120
#
################################################################################

def Factorial(iNo):
	i = 0
	j = 0
	Fact = 1

	for i in range(1,iNo+1,1):
		Fact = Fact * i	
        
	return Fact

def main():
	iValue = 0
	iRet = 0

	print("Enter the Number : ")
	iValue = int(input())

	iRet = Factorial(iValue)
	print("Factorial is : ",iRet) 


if __name__ == '__main__':
	main()