the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
print elements

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

print range(1,11)*2 # creates fixed list that could be appended only

fam=['ahmed', 'ola', 'bilal']
fam[0]=['ahmed']	# to append a list inside list element must be changed from str to list
fam[0].append('mahmoud') 
print fam

i = 0
while True :
	if i == 20:
		exit(0) # to exit loop or func
	print i
	i+=1
