import threading

def Straight(iNo):

	for i in range(1,iNo+1):
		print(i)

def Reverse(iNo):

	for i in range(iNo,iNo >= 1,-1):
		print(i)


def main():

	no = int(input("Enter the Number : "))

	thread1 = threading.Thread(target = Straight, args = (no,)) 
	thread1.start()
	thread1.join()

	thread2 = threading.Thread(target = Reverse, args = (no,)) 
	thread2.start()
	thread2.join()

	print("End of Application.....")


if __name__ == '__main__':
		main()	