list1 = range(0,5)

del list1[1] # use del to delete element in a list
print list1

for x in list1:
    print x

print x	# can see that var x in for loop still has value
del x	# del use to delete var
# print x

mynum = 1 # its a global var

def func1():
    global mynum # writing global means confirm to change in the global var
    mynum = 2

def func2():
	mynum = 3 # global var changed inside func only but outisde still as it is 

print mynum # first global var
func1()
print mynum # var has been changed inside func and value confirmed
func2()
print mynum # var has been changed inside func but value not confimred

