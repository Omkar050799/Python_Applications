#2. Write a program which accept one number and display below pattern.
#Input : 4
#
#   *  *  *  *
#   *  *  *  *
#   *  *  *  *
#   *  *  *  *
#
#
################################################################################

def Pattern(iRow):
	i = 0
	j = 0

	for i in range(0,iRow,1):
		for j in range(0,iRow,1):
			print(end = "*\t")

		print("\n")	
        
    

def main():
	iNo1 = 0
	iNo2 = 0

	print("Enter the Row : ")
	iNo1 = int(input())


	Pattern(iNo1) 


if __name__ == '__main__':
	main()