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
	word = words.pop(0) # take off the given index and return it 
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