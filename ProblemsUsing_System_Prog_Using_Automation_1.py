# 
# 1.Design automation script which accept directory name and file extension from user. Display all
# files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.
#
###########################################################################################################

from sys import *
import os

def DisplayFiles(Directory,Name):

    iRet = os.path.splitext(Name)
    iRet = iRet[0]

    print(iRet)

    for filename in os.listdir(Directory):
        f = os.path.join(Directory,filename)
        if(os.path.isfile(f)):
                Extension = f
                SplitX = os.path.splitext(Extension)
                SplitX = SplitX[1]
                if(SplitX == iRet):                 
                    print(f)


def main():

    print("------------------- Marvellous Infosystem : Automation 1 ---------------------")
    print("Script Name : ",argv[0])
    print("Number of arguments accepted : ",len(argv)-1)

    if((len(argv) > 3) or (len(argv) < 2)):
        print("Invalid Number of Arguments.....")
        print("Use -u flag for ussage...")
        print("Use -h flag for Help.....")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage : Script is used to Check the Specific Files are present on to the Directory...")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : Name_Script First_Argument Second_Argument")
        print("First_Argument : Give the Specific Path of Directory where you wants to search files")      
        print("Second_Argument : Extention of file, EX - .txt or .py or Somthing else..")
        exit()

        
    try:
        
        DisplayFiles(argv[1],argv[2])

    except Exception:
        print("Exception while executing the script...")
        print("Please check the inpute or contact the developer...")        


# Starter of the automation script
if __name__ == '__main__':
        main()  