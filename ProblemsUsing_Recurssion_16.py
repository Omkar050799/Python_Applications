def Recur(i):
	iSum = 0

	while i > 0:
		iDigit = i % 10
		iSum = iSum + iDigit
		i = i % 10

	print(iSum)	
		

def main():

	Recur(879)

if __name__ == '__main__':
		main()	