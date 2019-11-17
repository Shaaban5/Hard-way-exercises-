my_name = 'Ahmed'
my_age = 35 
my_height = 176 
my_weight = 70 
my_eyes = 'Blue'	
my_teeth = 'White'	
my_hair = 'Brown'  

# %s for str, %d for num, %r for the expersion as it is
# will be replaced in order

print ("Let's talk about %s." % my_name)
print ("He's %d cm tall." % my_height)
print ("He's %d kilo gram ." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair)) # in order
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)) # could be mixed 