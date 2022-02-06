# 
# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.
# After execution this script each .txt file gets renamed as .doc.
#
###########################################################################################################

from sys import *
import os

def DisplayFiles(Directory,FirstFile,SecondFile):

    iRet = os.path.splitext(FirstFile)
    iRet = iRet[0]

    iRet1 = os.path.splitext(SecondFile)
    iRet1  = iRet1[0]

    for filename in os.listdir(Directory):
        f = os.path.join(Directory,filename)
        if(os.path.isfile(f)):
                Extension = f
                SplitX = os.path.splitext(Extension)
                SplitX = SplitX[1]                  
                if(f.endswith(iRet)):
                    iRet2 = os.path.splitext(f)
                    LastFile = iRet2[0]
                    os.rename(f,LastFile + iRet1)    

    print("The Given directorys",iRet,"files gets coverted into",iRet1,"files")                 


def main():

    print("------------------- Marvellous Infosystem : Automation 1 ---------------------")
    print("Script Name : ",argv[0])
    print("Number of arguments accepted : ",len(argv)-1)

    if((len(argv) > 4) or (len(argv) < 2)):
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
        print("Second_Argument : Extention of file for Convert, EX - .txt or .py or Somthing else..")
        exit()

        
    try:
        
        DisplayFiles(argv[1],argv[2],argv[3])

    except Exception:
        print("Exception while executing the script...")
        print("Please check the inpute or contact the developer...")

    print("Application gets Terminated.....")            


# Starter of the automation script
if __name__ == '__main__':
        main()  