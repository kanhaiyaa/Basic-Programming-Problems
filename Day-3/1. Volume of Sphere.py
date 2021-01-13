#Formula for volume of shpere is - 4/3*pi*radius*3
import math
def vol_of_sphere(radius):
  return 4/3*math.pi*radius**3

vol_of_sphere(float(input("Enter the radius of sphere: ")))
