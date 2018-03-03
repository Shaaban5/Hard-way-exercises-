from sys import argv

script, first, second, third = argv

print "The script is called:", script # on command line gives the file name
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# at the command line type the file name.py followed by 3 variable name and
# output will will be the above printed str followed by your variable names.

# below is another way to add names to the str
print raw_input("The script is called:")
print raw_input("Your first variable is:")
print raw_input("Your second variable is:")
print raw_input("Your third variable is:")