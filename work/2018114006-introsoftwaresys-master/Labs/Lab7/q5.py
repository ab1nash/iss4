#taking input a single string with comma seperated
#eg: 2018,2,28,2019,2,28
import datetime
def GetDays(x,y):
	diff = y - x
	return(diff)

x=input()
x=x.split(',')
oneday = datetime.date(int(x[0]), int(x[1]), int(x[2]))
otherday = datetime.date(int(x[3]), int(x[4]), int(x[5]))
print(GetDays(oneday,otherday))