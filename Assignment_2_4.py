#4.Write a program which accept one number form user and return addition of its factors.
#Input :12
#Output : 16
#
################################################################################

def Factors(iNo):
	i = 0
	j = 0
	Fact = 0

	for i in range(1,iNo,1):
		if((12%i) == 0):
			Fact = Fact + i
			
        
	return Fact

def main():
	iValue = 0
	iRet = 0

	print("Enter the Number : ")
	iValue = int(input())

	iRet = Factors(iValue)
	print("Addition of Factors is : ",iRet) 


if __name__ == '__main__':
	main()