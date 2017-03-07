'''
Created on 07-Mar-2017

@author: srayabar
'''
cars = 100
drivers = 30
space_in_a_car = 3.0
car_pool_capacity = cars * space_in_a_car
passesngers = 90
average_passengers_per_car = passesngers / (cars - drivers)

print "Total cars", cars, "are driven"
print "We need to put",average_passengers_per_car,"in each car"