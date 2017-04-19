from sys import argv; from os.path import exists;scriptName, sourceFileName, targetFileName = argv; open(targetFileName, 'w').write(open(sourceFileName).read());

#print "Copying file contents from %s to %s" % (sourceFileName, 
#	targetFileName)

#print "Source file length - %d bytes" % len(sourceContent)

#print "Target file exists? %r" % exists(targetFileName)
#raw_input("Hit ENTER to continue, CRTL-C to CANCEL")

#print "Copy complete!"