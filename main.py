# With help from using the outcome from project 7, we will calculate the distance a beam of light travels in a year (light year):

# Initialize the following variables:
# Minutes in a year = (see project 7)
# Seconds in a minute = 60
# Light distance per second = 3 * 10^8 (in meters per second)
minutesOfYear = 525600
secondsOfMinute = 60
lightPerSecond = 3 * (10 ** 8)

# Compute how many seconds are in a year using the formula:
# Seconds in a year = Minutes in a year * Seconds in a minute
secondsOfYear = minutesOfYear * secondsOfMinute

# Compute the distance of a light year using the formula:
# Light year = Light distance per second * Seconds in a year
lightYear = lightPerSecond * secondsOfYear

# Print the light year (in meters)
print("A beam of light can travel " + str(lightYear) + " meters in a year.")