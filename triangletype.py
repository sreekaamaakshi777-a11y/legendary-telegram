#Type of triangle
def triangle_type(a,b,c):
    if a==b==c:
        return "This triangle is equilateral"
    elif a==b or b==c or a==c:
        return "This triangle is isosceles"
    else:
        return "This triangle is scalene"
    
print(triangle_type(12,12,12))
print(triangle_type(12,12,13))
print(triangle_type(12,13,14))