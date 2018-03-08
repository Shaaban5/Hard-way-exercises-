people = 30
cars = 40
buses = 15

# in order 'elif','else' are connected to first 'if' and will apply after 'if' result...
if cars > people:
	print "We should take the cars."
elif cars > people:
	print "We should not take the cars."
else:
	print "We should not decide."


# if elif changed to if connection lose with 1st if, and start new if code.
if cars > people:
	print "We should take the cars."
if cars > people:
	print "We should not take the cars."
else:
	print "We should not decide."
