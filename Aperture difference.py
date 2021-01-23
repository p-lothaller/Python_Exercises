import math

# Returns the stops of difference between the two given aperture values
# Round the answer to 1 decimal place
def stops_difference(aperture1, aperture2):
    aperture_base = math.sqrt(2)
    stop1 = math.log(aperture1)/math.log(aperture_base)
    stop2 = math.log(aperture2)/math.log(aperture_base)
    difference = stop2 - stop1
    return round(difference,1)


print(stops_difference(4, 2.8))
