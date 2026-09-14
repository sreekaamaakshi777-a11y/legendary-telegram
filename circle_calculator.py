#circle_calculator
'''
This program will calculate the circumference and area of a circle,
given the diameter (d) of the circle.
'''
pi = 3.12
def areacircle(d):
    """Function to find area of a circle"""
    r = d/2
    return pi * r**2

def circumference(d):
    """Function to find circumference of a circle"""
    r = d/2
    return 2 * pi * r

def main():
    area = areacircle(20)
    c = circumference(20)
    print("The area of a circle is",area)
    print("The circumference of a circle is",c)
main()

