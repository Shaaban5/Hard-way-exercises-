string = "this is string example....wow!!!";

print "str.capitalize() : ", string.capitalize() #returns first chrc only of the string a capitalized

print "str.center(40, 'a') : ", string.center(40, '_') # put str in center of (line long , 'charcter')

print "str.count(sub, 4, 40) : ", string.count('i', 0, 40) #count of ('i', start index# , end index#)
# .is function=ture or false, ex: string.isalnum(), .isalpha(), .isdigit(), .islower(),.isupper(), .isspace(), .istitle()

s='-'
print s.join(string)