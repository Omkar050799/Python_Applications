#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3
#
################################################################################

def CountFreq(value,iNo2):
	
	iCnt = 0
	for i in range(len(value)):
		
		if(value[i] == iNo2):
			iCnt = iCnt + 1
				
	return iCnt		


def main():
	iNo1 = 0
	iNo2 = 0
	data = []

	print("Enter the size of List : ")
	iNo1 = int(input())

	print("Enter the list Elements : ")
	for i in range(iNo1):
		data.append(int(input()))

	print("Enter the Number for Check Frequency : ")
	iNo2 = int(input())	

	iRet = CountFreq(data,iNo2)

	print("The frequency of the given Number is : ",iRet)	


if __name__ == '__main__':
	main()