string = "this is STRING example....WOW!!!";

print "str.capitalize() : ", string.capitalize() #returns first chrc only of the string a capitalized
print "STR.LOWER() : ", string.lower() #returns all str with lower letters

print "str.center(40, 'a') : ", string.center(40, '_') # put str in center of (line long , 'charcter')

print "str.count(sub, 4, 40) : ", string.count('i', 0, 40) #count of ('i', start index# , end index#)
# .is function=ture or false, ex: string.isalnum(), .isalpha(), .isdigit(), .islower(),.isupper(), .isspace(), .istitle()

s='-'
print s.join(string)

print '000word ss000'.strip('0') # erase the given charc from beg and end of the word
# defualt earse spaces in beg and end of the phrase

def test():
    return 'test'
T = test # we changed the function name to another name
print T()
TS = test() # we assigned function value to a var
print TS

int(round(1.2)) # int() return integre only and round() return 1.6 to 2.0 or 1.2 to 1.0
'_________________________________________________'

''' with & as
used for quick action with objectes without assigning variables or func
ex: here we created file for certain purpose then closed it without many lines
with open('new folder/test.py' , 'w') as f :
	f.close()										'''
'_________________________________________________'

list1 = [1, 2, 3, 4, 5, 6]
list1.append(7) # add to the end
list1.extend([8,9]) # = list1 + list2 # it change list1 to extended list
list1.remove(4)
list1.insert(3,4) # (index, obj) insert an element in a list at the given index
list1.reverse()	# reverse the list order
print list1
print list1[::-1] # return list started from : to : and read as -1 (this like reverse)

list1.sort()	#  it sort the list element as numb then alphabit
print list1.pop() # remove and return last element defalut is -1 or given your index 
print list1

# print list1[0][2] this print element indexed 0 then element indexed 2 inside it
# .reverse() = list1[::-1]
'_________________________________________________'

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new = [i for i in a if i%2 != 0] # creating a list with condition 
# creat list with i that cames from a[:] list and return only with if condition

x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b%2 != 0] # a for list x & b for list y then if condition
'_________________________________________________'
n = 4
check = {True: "Not Weird", False: "Weird"}	# dict to print certain str if result True of False
print check[ n%2 == 0 and ( n in range(2,6) or n > 20 ) ] # printing from dict with condition
# n in range() is a condition
# condition and ( condition or condition )
'_________________________________________________'
'''
map(func, list ) # its apply a func to each element in a list and return the processed list
to use quick func, use lambda as a quick un-pre defined func '''
list2 = map( lambda x: x*2 , list1)
print list2

# filter is like map and return the filtered elements as per given fun or lambda qucik func
print filter( lambda x : x < 10, list2) # all num below 10 exist in list 2
print filter (lambda x: x in list1, list2) # all num in list1 exist in list2
# = print [x for x in list1 if x in list2]
'_________________________________________________'

if 1 and 2 :		# 1 or any num consider as true case
	print True

if 0 :		# here 0 only consider as false
	print True
else :
	print False
'_________________________________________________'
# quick test (mad_lib)
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_string=ml_string.split()
    x=0
    for word in ml_string:
        if word_in_pos(word, parts_of_speech) != None:
            word=word.replace(word_in_pos(word, parts_of_speech),'corgi')
            replaced.append(word)
        else:
            replaced.append(word)
        x+=1
    new=" ".join(replaced)
    return new
    # your code here
    
print play_game(test_string, parts_of_speech)       
'_________________________________________________'

#good way to start loop and stop:
loop = True 
while loop :
	print 'the loop is working fine'
	loop = False

