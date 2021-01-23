

# Calculates the amount of seconds in the given amount of hours + minutes + seconds
def time_to_seconds(hours, minutes, seconds):
    total_seconds = hours*60*60 + minutes*60 + seconds
    return total_seconds


# Returns the amount of miles represented by the given amount of km
def km_to_miles(km):
    miles = km/1.61
    return miles


# Returns the average speed in miles per second of the given distance in km and time in hours, minutes and seconds
def avg_speed(km, hours, minutes, seconds):
    average = km_to_miles(km)/time_to_seconds(hours, minutes, seconds)
    return average

print(avg_speed(214,23,16,6))
