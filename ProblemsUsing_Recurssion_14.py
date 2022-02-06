def Recur(i):

	if i > 0:
		print(i)
		i -= 1 	
		Recur(i)
	

def main():

	Recur(5)



if __name__ == '__main__':
		main()	