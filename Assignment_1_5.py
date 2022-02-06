def Display(iValue):
	i = 0

	for i in range(iValue,0,-1):
		print(i)


def main():
	iNo = 0

	print("Enter the Range to see the Reverse Numbers from that Number : ")
	iNo = int(input())

	Display(iNo)


if __name__ == '__main__':
		main()	