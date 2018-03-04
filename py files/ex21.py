def add(a, b):
	print "ADDING %d + %d" % (a, b)	# incase i hashed# it, it stop the print msg only but the value still same
	return a + b
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"
age = add(30, 5)  		# once func called it give the print if it contain print
height = subtract(78, 4) # if u pressed caps lock + tab it will change first charc to uppercase
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,add(1,1))))) # func starting as inside out (from deepest to first)

print "That becomes: ", what, "Can you do it by hand?"