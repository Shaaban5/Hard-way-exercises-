list1 = range(0,5)

del list1[1] # use del to delete element in a list
print list1

for x in list1:
    print x

print x	# can see that var x in for loop still has value if its in a fucn value will be lost
del x	# del use to delete var
#print x # if printed error 'x' is not defined
'_______________________________________________'
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
'_______________________________________________'

assert 2 < 5, 'problem' # assert or assert not expression , then error 'msg' i want
# assert not 2 < 5 , 'wow its working'
'_______________________________________________'

mylist = [x+1 for x in range(3)] # creates list as equation 'x+1' for every x in range(3) will be added to 1
print mylist

new = [[x+1] for x in range(3)] # creates an individual list for each element 
print new

generator = (x+1 for x in range(3)) # generator is a list but for loop purpuse only and it use () not []
for i in generator:
	print i
print generator

# Return sends a specified value back to its caller whereas Yield can produce a sequence of values. 
'_______________________________________________'
a=5
print eval('a + 50') # eval run and equation inside str
exec('a = 50 + 5') # assign var inside str
print a
'_______________________________________________'

#if 5 != 4:
    #raise Exception('mmm it looks like assert') 
'_______________________________________________'
for letter in 'Python':
   if letter == 'h':
      continue # the oppiset of break where when the rule apply doent let the loop continue do- 
      		   # ing what its doing and force it to continue the next loop.
   print 'Current Letter :', letter
'_______________________________________________'
# else statement could be used with while & for loop just like if 'used when loop become false'
'_______________________________________________'
dict = {'Name':'Zara', 'Age':7, 'Class':'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
#del dict['Name']; # remove entry with key 'Name'
#dict.clear();     # remove all entries in dict
#del dict ;        # delete entire dictionary

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
print dict



















