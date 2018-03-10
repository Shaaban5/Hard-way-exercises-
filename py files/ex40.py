# Class is a bluprint that could be used as a desgin to be clone
# remember using (python file name argument1 argument2 ...) as a script 
# its look like it but using it inside python
# 1st make the initial definition of arguments and var that will be used
class Song():		# better to name the Class as 1st upper letter
	def __init__(self, words):	# self here represent class name
		self.lyrics = words  	# as Song.lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def count_lines(self):
		print len(self.lyrics)

# making a clone called happy_bday
happy_bday = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

happy_bday.sing_me_a_song() # calling func sing_me..
print len(happy_bday.lyrics) # using the self.lyrics outside func
happy_bday.count_lines()

bulls_on_parade.sing_me_a_song()
print len(bulls_on_parade.lyrics)
bulls_on_parade.count_lines()