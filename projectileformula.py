# Part 3 FORMULA

# math methods required for this calculation
from math import pi, tan, cos

# INITIAL CONDITIONS

# g is acceleration due to gravity, 9.81m/s^2
g = 9.81

# VARIABLES TO BE INPUT BY USER:
# v0 is the initial velocity of the projectile in m/s
# deg is the elevation angle of the barrel in degrees, which needs converting to radians
# x is the horizontal distance travelled by the projectile in metres
# y0 is the height of the barrel in metres

v0 = float(input("Please enter a value for initial velocity in m/s: "))
deg = float(input("Please enter a value for the elevation angle of the barrel in degrees: "))
y0 = float(input("Please enter a value for the height of the barrel: "))
x = float(input("Please enter a value for the horizontal distance travelled in metres: "))

# Convert degrees to radians
theta = deg*(pi/180)

# Formula for the height (y) of a projectile
y = y0 + x*tan(theta) - (g*x**2/(2*(v0*cos(theta))**2))

# Show the answer to the problem
print("The height of the projectile is: ", y, "metres")

