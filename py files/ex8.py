formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

print formatter % ("I had this thing."
	,"That you could type up right.",
	"But it didn't sing."
	,"So I said goodnight."
	) # make several lines


name = input("What is your name: ")
age = input("How old are you: ")
age=int(age)
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)