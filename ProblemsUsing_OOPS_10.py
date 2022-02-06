class BankAccount:

	ROI = 10.5

	def __init__(self,a,b):
		self.Name = a
		self.Amount = b
	
	def Deposit(self,Depo):

		self.Amount = Depo
		
		Display(Name,Depo)
	

	def Withdraw(self,With):

		self.Amount = With
		Display(Name,With)
		

	def CalculateInterest(self,Year):

		self.ROI = ROI * Amount * Year
		print("ROI for Your account : ",ROI)



	def Display(self,Navv,Paisa):

		print("Name Of Coustomer : ",Navv)

		print("Amount Updated : ",Amount)


def main():

	obj1 = BankAccount()

	obj1.Deposit("Omkar Malpote",15000)
	obj1.Deposit("Santosh Shinde",200000)

	obj1.Withdraw("Omkar Malpote",5000)
	obj1.Withdraw("Santosh Shinde",6000)



if __name__ == '__main__':
		main()	