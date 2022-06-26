def liters_100km_to_miles_gallon(liters):
    km_mile = 100000/1609.344
    liter_gallon = liters/3.785411784
    return km_mile/liter_gallon

#
# Write your code here.
#

def miles_gallon_to_liters_100km(miles):

  return 235.215/miles
  
  
  
  
#
# Write your code here
#
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
