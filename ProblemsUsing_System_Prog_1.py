import os

def main():

    Name = input("Enter the file to check its prensent on directory or not : ")

    bRet = os.path.isfile(Name)

    if(bRet == True):
        print("The file is present in directory...")
    else:    
        print("The file is not present in directory....")
        

if __name__ == '__main__':
    main()
