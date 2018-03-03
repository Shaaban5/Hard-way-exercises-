print 'How old are you?', # comma has been added to continue print in same line
age=raw_input()   # diff raw_input() type it raw inside str & input() type it num
print 'how tall are you?',
tall=int(raw_input())	# int() convert str to integer incase str are nums

weight=input('How much do you weight?')	# prompt msg to enter the data

print 'so your are %r years old, %r tall, %r weight.'%(age, tall, weight)

# python -m pydoc raw_input <- typr this in normal terminal and read some comment from pydoc
