tabby_cat = "\tI'm tabbed in"
persian_cat = "I am split \non a line"
backslash_cat = "I'm \\a \\ cat"

fat_cat = '''
I'll do a list
\t* Cat food
\t* Fish
\t* Cat food\n\t* something else
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "%r" % fat_cat