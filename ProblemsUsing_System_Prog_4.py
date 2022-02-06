from filecmp import *
import os
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,"rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def main():

    Name1 = input("Enter the First file name : ")

    Name2 = input("Enter the Second file name : ")

    iRet1 = hashfile(Name1)

    iRet2 = hashfile(Name2)

    print(iRet1)
    print(iRet2)


    if(iRet1 == iRet2):
        print("The Files are having Same Data init...")
    else:
        print("The Files are Dosent having Same Data init... ")    


if __name__ == '__main__':
    main()
