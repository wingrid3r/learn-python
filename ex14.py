from sys import argv

#get the arguments
scriptName, yourName = argv
#define prompt
prompt = "$ "

#use the arguments to get more input from the user
print "Hello %s! \nI am %s - the Script \n" % (yourName, scriptName)
#print "What is the meaning of %s" % yourName, 
#trying something different
meaningOfName = raw_input("What is the meaning of " 
	+ yourName + "? " + prompt)
print "Where are you from %s" % yourName, 
nativePlace = raw_input(prompt)
print "What is your hobby %s?" %yourName, 
yourHobby = raw_input(prompt)

#put everything together
print """
The script - %s captured following info about you.
You are %s which means %s.
You are from %s.
Your main hobby is %s.
""" % (scriptName, yourName, meaningOfName, nativePlace, yourHobby)