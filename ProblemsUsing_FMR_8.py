################################################################################################################
#
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 0. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000
#
################################################################################################################

from functools import reduce

"""
def CheckBig(no):
    if((no >= 70) and (no <= 90)):
        return True
    else:
        return False
"""

CheckBig = lambda no: ((no >= 70) and (no <= 90))        

"""
def Increament(no):
    return no + 10
"""

Increament = lambda no: (no + 10)

"""
def Multiplication(a,b):
    return a * b
"""

Multiplication = lambda a,b: (a * b)

def main():
    
    iNo = 0
    data = []

    print("Enter the how many elements you want :")
    iNo = int(input())

    print("Enter the elements :")
    for i in range(iNo):
    	data.append(int(input()))

    print("Original Data is : ",data)
    
    # filter(Function,list)
    newdata = list(filter(CheckBig,data))
    print("Data After Filter : ",newdata)    
   
    # map(Function,list)    
    increamentdata = list(map(Increament,newdata))
    print("Data After map : ",increamentdata)
    
    # reduce(Function,,list)
    ret = reduce(Multiplication,increamentdata)
    print("Data after reduce : ",ret)
    
if __name__ == "__main__":
    main()