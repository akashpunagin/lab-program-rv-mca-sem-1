from math import pi

try:
    radius = int(input("Enter radius of circle: "))

    area = pi * radius * radius
    print("Area of circle is:", area)

except ValueError as e:
    print("Radius should be an integer")
except Exception as e:
    print("Error occured. Please try again")
