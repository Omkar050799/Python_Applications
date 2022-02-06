#3.Write a program which accept N numbers from user and store it into List. Return Minimum
#number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7 
#Output : 5
#
################################################################################

def FindMin(value):
	iMax = 0
	iMin = 0

	for i in range(len(value)):
		if(iMax < value[i]):
			iMax = value[i]
			iMin = iMax

	for i in range(len(value)):
		if(iMin > value[i]):
			iMin = value[i]		

	return iMin		

def main():
	iNo = 0
	data = []


	print("Enter the Size of list : ")
	iNo = int(input())

	print("Enter the list element : ")
	for i in range(iNo):
		data.append(int(input()))

	iRet = FindMin(data)
	
	print("The Minimum Number is : ",iRet)	



if __name__ == '__main__':
	main()