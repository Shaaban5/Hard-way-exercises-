def break_words(stuff):
	"""This function will break up words for us.""" # ''' documentation you import .py this sentence appeares in help(filename)
	words = stuff.split() # create list and defulat parameter is space
	return words
print break_words('ahmed ola bilal')

def sort_words(words):
	"""Sorts the LIST from NUMS, space, a, b, .... z."""
	return sorted(words) 
print sort_words(['ahmed', 'ola', 'bilal', 19,30,44])

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0) # take off the given index from a list if no index givien it consider last elemnet '-1'
	print word 			
	print words 		# the list will be cutted
print_first_word(['ahmed','ola','bilal'])

# list.remove('str') delete the given str from list (error will apply if no such str)

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-3) #[ 0, 1 , 2]
	print word 			 #[-3, -2,-1]
	print words
print_last_word(['ahmed','ola','bilal'])

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
print sort_sentence('ahmed ola bilal')

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t1The lovely world 1
with logic so 1 firmly planted
cannot discern \n the needs 1 of love
nor comprehend passion from 1 intuition
and requires 1 an explantion
where there 1 is none.
"""

"""  # using quot or double quot without assigning to var used as documentaion
"""
print poem.find('1',poem.find('1', poem.find('1', poem.find('1')+1)+1)+1) # find(1, comes after find(1)+1)
# find('str', start index, end index) return -1 if doesnt find the require
print poem.index('1',poem.index('1', poem.index('1')+1)+1) 
# same just like .find() but it raise an error if didnt find the required

# print poem.replace('1', '2' , 2 ) # print str and replace('str', with given 'str', 2 times only)
print poem.count('1') # check how many count of given str


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)


sentence = "All good\tthings come to those who wait."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)