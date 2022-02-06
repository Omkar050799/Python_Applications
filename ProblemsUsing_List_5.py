################################################################################################################
#
# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)
#
################################################################################################################

import Marvellous as M

def ListPrime(value):
	iSum = 0
	i = 0
	iRet = False

	for i in range(len(value)):
		iRet = M.ChckPrime(value[i])
		if(iRet == True):
			iSum = iSum + value[i]				
                   
	return iSum				


def main():
	iNo1 = 0
	iNo2 = 0
	data = []

	print("Enter the size of List : ")
	iNo1 = int(input())

	print("Enter the list Elements : ")
	for i in range(iNo1):
		data.append(int(input()))

	print("Above is Prime")		

	iRet = ListPrime(data)

	print("The Addition of all prime Numbers : ",iRet)	


if __name__ == '__main__':
	main()