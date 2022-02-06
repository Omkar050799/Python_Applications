import threading

def ChkSmall(DataX):
	iCnt = 0 

	for i in range(len(DataX)):
		if(DataX[i] >= 'a' and DataX[i] <= 'z'):
			iCnt = iCnt + 1

	print("The Small Latters are : ",iCnt)	


def ChkCap(DataX):
	iCnt = 0

	for i in range(len(DataX)):
		if(DataX[i] >= 'A' and DataX[i] <= 'Z'):
			iCnt += 1

	print("The Capital Latters are : ",iCnt)		


def ChckNum(DataX):
	iCnt = 0

	for i in range(len(DataX)):
		if(DataX[i] >= '0' and DataX[i] <= '9'):
			iCnt += 1

	print("The Digits are : ",iCnt)		

def main():

	Name = str(input("Enter the Name : "))

	Smallthread = threading.Thread(target = ChkSmall, args = (Name,)) 

	Smallthread.start()

	CapThread = threading.Thread(target = ChkCap, args = (Name,))

	CapThread.start()

	DigitThread = threading.Thread(target = ChckNum, args = (Name,))

	DigitThread.start()

	Smallthread.join()
	CapThread.join()
	DigitThread.join()


if __name__ == '__main__':
		main()	