#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.
#
##############################################################################################################

import Arithematic

def main():
	
	print("Enter the First element : ")
	iValue1 = int(input())

	print("Enter the Second element : ")
	iValue2 = int(input())
    
	    iRet1 = Arithematic.Add(iValue1,iValue2)
	    	print("The Addition is : ",iRet1)

	    iRet2 = Arithematic.Sub(iValue1,iValue2)
	    	print("The Addition is : ",iRet2)

	    iRet3 = Arithematic.Mult(iValue1,iValue2)
	    	print("The Addition is : ",iRet3)

	    iRet4 = Arithematic.Div(iValue1,iValue2)
	    	print("The Addition is : ",iRet4)


if __name__ == '__main__':
	main()