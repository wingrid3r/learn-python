#tip calculator
food = 43
tax = 6.75
tip = 15.0
#calculate tax, tip and total
tax_amount = food * (tax / 100)
tip_amount = (food + tax_amount) * (tip / 100)
food_with_tax = food + tax_amount
total_amount = food_with_tax + tip_amount
#print
print "Itemized bill"
print "Food:", food
print "Tax @%.2f: %.2f" %(tax, tax_amount)
print "Amount with tax:", food_with_tax
print "Tip @%.2f: %.2f" %(tip, tip_amount)
print "Total:", total_amount