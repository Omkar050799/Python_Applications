def Display(iNo):
	i = 0

	for i in range(iNo+iNo):
		if((i % 2) == 0):
			print(i)


def main():
	iValue = 0

	print("Enter the Range to Display")
	iValue = int(input())

	Display(iValue)


if __name__ == '__main__':
	main()