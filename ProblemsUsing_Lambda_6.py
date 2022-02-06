################################################################################################################
#
# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input  : 4     Input : 16 
# Output : 16   Output : 64
#
################################################################################################################

powerX = lambda no : ((no ** 2)*no)

def main():

	iNo = 0
	iret = 0

	print("Enter the Number : ")
	iNo = int(input())

	iret = powerX(iNo)

	print("The Power of Given Number : ",iret)

if __name__ == '__main__':
		main()	