def printTwo(*args):
	input1, input2 = args
	print "Input 1: %s\nInput 2: %s" % (input1, input2)

def printTwoAgain(arg1, arg2):
	print "Input 1: %s\nInput 2: %s" % (arg1, arg2)
	
def printOne(arg1):
	print "Only input is %s" %arg1
	
def printNone():
	print "Nothing to see here."
	
	
printTwo("Whats'Up", "Nothing Much")
printTwoAgain('Wazaaaaaaaaaap', 'Wazaap')
printOne('Yo!')
printNone()