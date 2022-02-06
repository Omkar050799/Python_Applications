def Pattern(iNo):
	for i in range(iNo):
		print(end ="*\t")

	print("\n")

def main():
	iValue = 0

	print("Enter the Number")
	iValue = int(input())

	Pattern(iValue)


if __name__ == '__main__':
	main()