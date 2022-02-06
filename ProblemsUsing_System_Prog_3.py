def main():

    Name = input("Enter the File name to create : ")

    fd = open(Name,"x")

    NameRead = input("Enter the File Name for open : ")

    fd2 = open(NameRead,"r")

    data = fd2.read()

    fd.write(data)

    print("Data gets Succefully Copied from 1 file to another file")


if __name__ == "__main__":
    main()
