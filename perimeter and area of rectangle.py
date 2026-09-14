#perimeter and area of rectangle
l = int(input("Enter length here: "))
b = int(input("Enter breadth here: "))
def rectangle_area(l,b):
    return l*b

def rectangle_perimeter(l,b):
    return 2*(l+b)

def main():
    area = (rectangle_area(l,b))
    print("The area of the rectangle is",area)
    perimeter = (rectangle_perimeter(l,b))
    print("The perimeter of the rectangle is",perimeter)
main()