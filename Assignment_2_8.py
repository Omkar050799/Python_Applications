#2. Write a program which accept one number and display below pattern.
#Input : 5
#
#
#                       _____1______2_______3______4
#   1                  1|   (1,1)  (1,2)   (1,3)  (4,4)
#   1  2               2|   (2,1)  (2,2)   (2,3)  (4,4)
#   1  2  3            3|   (3,1)  (3,2)   (3,3)  (4,4)
#   1  2  3  4         4|   (4,1)  (4,2)   (4,3)  (4,4)
#   1  2  3  4  5      5|   (5,1)  (5,2)   (5,3)  (5,4)
#
################################################################################

def Pattern(iRow):
	i = 0
	j = 0

	for i in range(1,iRow+1):
		for j in range(1,iRow+1):
			if(j<=i):
				print(j,end = " ")
			else:
				print(" ")	
						

def main():
	iNo = 0

	print("Enter the Row")
	iNo = int(input())

	Pattern(iNo)


if __name__ == '__main__':
	main()