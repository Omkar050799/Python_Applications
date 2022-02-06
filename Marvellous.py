def ChckPrime(iNo):
	iRange = iNo
	i = 0
	Sign = True

	if(iNo == 1):
		return True
    
	for i in range(2,iRange):
		if((iNo % i) == 0):
			Sign = False
			return Sign
	
	print("Primes",iNo)
	return Sign	
