def Display(iName):
	Count = 0

	Count = len(iName)
	return Count 



def main():
	
	iRet = 0


	print("Enter the Range to Display")
	iName = (input())

	iRet = Display(iName)
	print(iRet)
    
    


if __name__ == '__main__':
	main()