#Area of a rectangle
def arearectangle(length, width): #Here, length & width are parameters
    result = length * width #result is the variable
    print("The area of the rectangle is ", result)
arearectangle(5,2) #Function call
#arguments are 5 & 2

#Area of a circle
def areacircle(radius):
    result = 3.14 * radius**2
    print("The area of the circle is ",result)
areacircle(10)

#Area of a square
def areasquare(side):
    result = side**2
    print("The area of the square is ",result)
areasquare(10)

#Area of triangle
def areatriangle(base,height):
    print("The area of the triangle is", 1/2 * base * height)
areatriangle(10,10)

def main():
    area = arearectangle(5,2)
    area = areacircle(10)
    area = areasquare(10)
    area = areatriangle(10,10)
    print(area)
main()