def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates # check the order despite off the var names


start_point = 10000
beans, jars, crates = secret_formula(start_point) # here we made script with order and assigned to func
# var name could be changed but order is important

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) # we calling the assigned script

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # another way to calling it

def family(a,b,c):
	dad=a
	mom=b
	son=c
	return dad,mom,son

print family('ahmed', 'ola', 'bilal')
x,y,z=family('ahmed', 'ola', 'bilal')
print 'dad is %s, mom is %s, son is %s' % (x,y,z)
print 'dad is %s, mom is %s, son is %s' % family('ahmed', 'ola', 'bilal')