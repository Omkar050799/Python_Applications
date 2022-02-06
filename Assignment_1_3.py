def Add(iValue1,iValue2):
	return iValue1 + iValue2

def main():
	iNo1 = 0
	iNo2 = 0
	iRet = 0

	print("Enter the firs Number : ")
	iNo1 = int(input())

	print("Enter the Second Number : ")
	iNo2 = int(input())

	iRet = Add(iNo1,iNo2)

	print("Addition is : ",iRet)



if __name__ == '__main__':
		main()	