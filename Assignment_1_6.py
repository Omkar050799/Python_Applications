def Display(iNo):

	if(iNo < 0):
		print(iNo, " is Negative Number")
	elif(iNo > 0):
	    print(iNo, " is Positive Number")
	else:
	    print(iNo, " is Zero")    	


def main():
	iValue = 0

	print("Enter the Value to check its Behaviour : ")
	iValue = int(input())

	Display(iValue)



if __name__ == '__main__':
	main()