#2.Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56
#
################################################################################

def FindMaxi(value):
	iMax = 0

	for i in range(len(value)):
		if(iMax < value[i]):
			iMax = value[i]

	return iMax		

def main():
	iNo = 0
	data = []


	print("Enter the Size of list : ")
	iNo = int(input())

	print("Enter the list element : ")
	for i in range(iNo):
		data.append(int(input()))

	iRet = FindMaxi(data)
	
	print("The Maximum Number is : ",iRet)	



if __name__ == '__main__':
	main()