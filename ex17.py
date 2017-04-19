from sys import argv
from os.path import exists

scriptName, sourceFileName, targetFileName = argv

print "Copying file contents from %s to %s" % (sourceFileName, 
	targetFileName)

sourceContent = open(sourceFileName).read()

print "Source file length - %d bytes" % len(sourceContent)

print "Target file exists? %r" % exists(targetFileName)
raw_input("Hit ENTER to continue, CRTL-C to CANCEL")

open(targetFileName, 'w').write(sourceContent)

print "Copy complete!"