cars = 100
drivers = 30
passengers = 115
space_per_car = 4
cars_not_ready = cars - drivers
cars_ready = drivers
carpool_capacity = cars_ready * space_per_car
passenger_per_car = passengers / cars_ready

print "There are ", cars, " cars in the depot"
print "But only ", drivers, " drivers are available"
print "So ", cars_not_ready, " cars are sitting idle"
print "We have ", passengers, " passengers ready to travel"
print "Our carpool_capacity is ", carpool_capacity
print "There will be about ", passenger_per_car, " passengers per car"
