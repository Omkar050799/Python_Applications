#1.Write a program which accept N numbers from user and store it into List. Return addition of all
#elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130
#
################################################################################

def Addition(Value):
	sum = 0

	for i in range(len(Value)):
		sum = sum + Value[i]

	return sum	

def main():

	iNo = 0
	Data = []

	print("Enter how many Element you want to save : ")
	iNo = int(input())

	print("Enter the Elements to store")
	for i in range(iNo):
		Data.append(int(input())) 
  
	iRet = Addition(Data)
    
	print("The Addition is : ",iRet)


if __name__ == '__main__':
	main()