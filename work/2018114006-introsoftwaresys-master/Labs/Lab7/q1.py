def isLeapYear(k):
	if(k%100==0):
		if(k%400==0):
			return True
		else:
			return False
	else:
		if(k%4==0):
			return True
		else:
			return False
x=input()
print(isLeapYear(int(x)))