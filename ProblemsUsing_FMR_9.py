################################################################################################################
#
#4.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204
#
################################################################################################################

from functools import reduce
"""
def CountEven(no):
    if((no % 2) == 0):
        return True
    else:
        return False
"""
CountEven = lambda no: ((no % 2) == 0)

"""
def Square(no):
    SQ = no ** 2
    return SQ
"""

Square = lambda no: ((no ** 2))

"""
def Addition(a,b):
    Add = a + b
    return Add
"""

Addition = lambda a,b: (a + b)

def main():
    iNo = 0
    data = []

    print("How many elements you want :")
    iNo = int(input())

    print("Enter the elements")
    for i in range(iNo):
        data.append(int(input()))

    print("Orignel Data : ",data)

    FilterData = list(filter(CountEven,data))
    print("Data after Filter:",FilterData)

    MapData = list(map(Square,FilterData))
    print("Data after Map :",MapData)

    ReduceData = reduce(Addition,MapData)
    print("Data after Reduce :",ReduceData)
  

    
if __name__ == "__main__":
    main()
