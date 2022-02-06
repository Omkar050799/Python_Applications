################################################################################################################
#
# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input  : 4   3    Input : 12 
# Output : 16  3   Output : 48
#
################################################################################################################

iMultX = lambda a,b : (a*b)

def main():

	iNo1 = 0
	iNo2 =0
	iRet = 0

	print("enter the fisrt number :")
	iNo1 = int(input())

	print("enter the second number :")
	iNo2 = int(input())

	iRet = iMultX(iNo1,iNo2)

	print("Multiplication is : ",iRet)


if __name__ == "__main__":
	main()	