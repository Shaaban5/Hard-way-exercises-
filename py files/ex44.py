class Parent(object): # can write object here to use super()
	def __init__(self, family_name, color):
		self.last = family_name
		self.color = color
	def implicit(self):
		print "PARENT implicit()"

class Child(Parent): # whats written inside () is the parent class and could be multiple parents (parent1, parentr2, ...)
	def implicit(self):	# making same func like parent mean to override the parent
		print 'Child override parent implicit()'
		super(Child, self).implicit()	# force the current class to use the parent func super
		print 'parent return to override'
		#pass # pass here means no block to be run and just pass it

dad = Parent('shaaban', 'semi white')
son = Child('shaaban', 'semi white') # to give more arguments u need to override parent.__init__ by creat its own init

dad.implicit()
son.implicit()

print son.last

# composition is dont use inhirtance and just use the other class func
# in above case in class Child when calling implicit() from parent we type
# self.parent.implicit() and self here represent child