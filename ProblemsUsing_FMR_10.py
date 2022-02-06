################################################################################################################
#
# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62
#
#
################################################################################################################

from functools import reduce

def ChkPrime(no):
    Sign = True
    for i in range(2,no):
        if((no % i) == 0):
            Sign = False
        
    return Sign        
        
def Multi(no):
    Mult = no * 2
    return Mult

def MaxiMum(a,b):

    if(a < b):
       return b
    else:
        return a   

def main():
    iNo = 0
    data = []

    print("How many elements you wants :")
    iNo = int(input())

    print("Enter the elements")
    for i in range(iNo):
        data.append(int(input()))

    print("Orignel data :",data)

    FilterData = list(filter(ChkPrime,data))
    print("Data after filter :",FilterData)

    MapData = list(map(Multi,FilterData))
    print("Data after Map :",MapData)

    reduceData = reduce(MaxiMum,MapData)
    print("Data after Reduce :",reduceData) 
    

if __name__ == '__main__':
    main()
