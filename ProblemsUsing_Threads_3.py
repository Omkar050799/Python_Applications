import threading

def EvenList(DataX):
	i = 0
	iSum = 0

	for i in range(len(DataX)):
		if((DataX[i] % 2) == 0):
			iSum = iSum + DataX[i]

	print("The Addition of Even Elements : ",iSum)
	
def OddList(DataX):
	x = 0
	iSum2 = 0

	for x in range(len(DataX)):
		if((DataX[x] % 2) != 0):
			iSum2 = iSum2 + DataX[x]

	print("The Addition of Odd Elements : ",iSum2)							


def main():

	data = []

	size = 0

	print("Enter the Size...")
	iNo = int(input())

	print("Enter the list Elements : ")
	for i in range(iNo):
		data.append(int(input()))

	thread1 = threading.Thread(target = EvenList, args = (data,))
	thread2 = threading.Thread(target = OddList, args = (data,))

	thread1.start()	
	thread2.start()
	



if __name__ == '__main__':
		main()	