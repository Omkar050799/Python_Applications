import threading

def EvenFactors(x):
	iSum = 0

	for i in range(x):
		if((i % 2) == 0):
			iSum = iSum + i
	
	print("Addition Of Even Factors :",iSum)		


def OddFactors(x):
	iSum = 0

	for i in range(x):
		if((i % 2) != 0):
			iSum = iSum + i

	print("Addition Of Odd Factors :",iSum)		


def main():

	iNo = 0

	iNo = int(input("ENter the Number : "))

	Thread1 = threading.Thread(target = EvenFactors,args = (iNo,))
	Thread2 = threading.Thread(target = OddFactors,args = (iNo,))

	Thread1.start()
	Thread2.start()

	Thread1.join()
	Thread2.join()

	print("End of Main...")



if __name__ == '__main__':
		main()	