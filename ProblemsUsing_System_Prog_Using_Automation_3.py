# 
# 3. Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp.
#
###########################################################################################################

from sys import *
import os
import shutil

def DisplayFiles(Directory1,Directory2):

    os.mkdir(Directory2)
    try:
        for filename in os.listdir(Directory1):
            f = os.path.join(Directory1,filename)
            if(os.path.isfile(f)):
                Extension = f
                SplitX = os.path.splitext(Extension)
                SplitX = SplitX[1]
                shutil.copy2(f, Directory2)                  
                print(f)    

        print("All files gets Succefully copy into",Directory2,"Directory")

    except Exception as e:
        print(e)        

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
        print("Second_Argument : Extention of file for Convert, EX - .txt or .py or Somthing else..")
        exit()

        
    try:
        
        DisplayFiles(argv[1],argv[2])

    except Exception:
        print("Exception while executing the script...")
        print("Please check the inpute or contact the developer...")

    print("Application gets Terminated.....")            


# Starter of the automation script
if __name__ == '__main__':
        main()  