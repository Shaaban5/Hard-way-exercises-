def print_args(*d):	# like script in ex 15 - 17 - * gives multiple arguments
	a1, a2, a3, a4 = d # assing as much as u can but consider the arguments inside () when you print
	print 'arg1: %r, arg2: %r, arg3: %r, arg4: %r' % (a1,a2, a3, a4)


ahmed='ahmed'
num=60

def print_again(arg1, arg2):
	print 'arg1: %r, arg2: %r' % (arg1,arg2)

def print_one(arg1):
	print 'arg1: %r' % arg1

def print_none():
	print 'nothing to print'


print_args(ahmed*5, 'ola', 'bilal',(50+10)*num) # variable and nums could be used
print_again(ahmed*3,"shaaban")
print_one("AHMED!!")
print_none()