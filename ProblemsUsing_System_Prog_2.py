def main():

	Name = input("Enter the File Name : ")

	fd = open(Name,"r")

	data = fd.read()

	print("The Data of File : ",data)


if __name__ == "__main__":
	main()	