def main():

    Name = input("Enter the file name : ")

    StringX = input("Enter for search...")

    fd = open(Name,"r")

    if (StringX in fd.read()):
        print("The word is Presnet..")
    else:
        print("The word is not Presnet..")    

    
if __name__ == '__main__':
        main()    