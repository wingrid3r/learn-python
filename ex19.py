def getSum(num1, num2):
	print "Sum of %d and %d is %d" % (num1, num2, 
		num1 + num2)
		
#direct
getSum(10, 20)

#using variables
num1 = 3 # <-- local to script
num2 = 6 # <-- local to script
getSum(num1, num2)

#using math
getSum(1 + 2, 3 + 4)

#using above all combos
getSum(num1 + 1, num2 + 3)