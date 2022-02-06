import threading

def EvenNumbers(x):

	for i in range(x):
		if((i % 2) == 0):
			print("Even : ",i)

def OddNumbers(x):
	
	for i in range(x):
		if((i % 2) != 0):
			print("Odd : ",i)			

def main():

	iNo = 0

	iNo = int(input("Enter the Number : "))

	Thread1 = threading.Thread(target = EvenNumbers,args = (iNo,))

	Thread2 = threading.Thread(target = OddNumbers, args = (iNo,))

	Thread1.start()
	Thread2.start()

	Thread1.join()
	Thread2.join()


if __name__ == '__main__':
		main()	