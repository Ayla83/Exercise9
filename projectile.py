# Part 3

# math methods required for this calculation
from math import pi, tan, cos

# INITIAL CONDITIONS

# g is acceleration due to gravity, 9.81m/s^2
# v0 is the initial velocity of the projectile in m/s
# deg is the elevation angle of the barrel in degrees, which needs converting to radians
# x is the horizontal distance travelled by the projectile in metres
# y0 is the height of the barrel in metres
g = 9.81
v0 = 44.0
deg = 80.0
x = 0.5
y0 = 1.0

# Convert degrees to radians
theta = deg*(pi/180)

# Formula for the height (y) of a projectile
y = y0 + x*tan(theta) - (g*x**2/(2*(v0*cos(theta))**2))

# Show the answer to the problem
print("The height of the projectile is: ", y, "metres")
