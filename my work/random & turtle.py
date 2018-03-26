import random

print random.randint(0, 5) * 2 # randint for integers num

print random.random() # random float num btw 0 & 1, it can be * 100 to be btw 0 & 100

list1 = [1, 3, '2', '5', 'black', 'car', 'food']
print random.choice(list1)	# random from list

random.shuffle(list1) # shuffle th elements inside list and change the original
print list1	

print random.randrange(0, 10, 2) # same like randint but with steps option

print random.sample(list1, 2) # random choice given# of element from given list
'________________________________________________'
import turtle

def square():
	window = turtle.Screen()
	window.bgcolor('dark red')

	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('light green')
	brad.speed(3)	# pointer speed from fastest 0 10 9 8 7 ...to 1 slowest 
	brad.dot(None, 'yellow') # home pointer (size, color) the first start only

	brad.fd(15) # fd() or forward()
	brad.left(90) # lt() left() angle
	brad.bk(50) # back() bk() backword()
	brad.right(90) # rt() right() angle
	brad.goto(0,0) # setpos() setposition
	brad.seth(90) # setheding() angle
	brad.home() # back home = goto(0, 0)
	brad.circle(50,None,10) # makes circle (radius, extent, steps)
	# if steps is 3 traingle if 4 square and so on
	bard.penup() # up() pu() turtle is up and can be move without drawing
	brad.pendown() # down() pd() turtle is on paper again and record every move

	brad.isdown() # return False or True regading the pen
	brad.position() # return the current position
	brad.heading()	# return current heading
	brad.distance(0,0) # return distance from turtle to th given (x, y)
	brad.toward(0,0) # return angle btw turtle and the given (x, y)



	window.exitonclick()

square()