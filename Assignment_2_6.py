#2. Write a program which accept one number and display below pattern.
#Input : 5
#
#   *  *  *  * *
#   *  *  *  *
#   *  *  *  
#   *  *   
#   *
#
################################################################################

def Pattern(iRow):
	i = 0
	j = 0

	for i in range(iRow+1):
		for j in range(iRow+1):
			if(i < j):
				print(end = "*\t")
			else:
				print(" ")			

def main():
	iNo = 0

	print("Enter the Row")
	iNo = int(input())

	Pattern(iNo)


if __name__ == '__main__':
	main()