import math

t = float(input("Enter the value of the temperature in Fahrenheit: "))
v = float(input("Enter the value of the wind speed in miles per hour: "))

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
print("The effective temperature of the wind chill is", w)