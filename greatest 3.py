#Greatest of three numbers
#Python code to compare which number is bigger
a = int(input("Enter the first number here: "))
b = int(input("Enter the second number here: "))
c = int(input("Enter the third number here: "))

if a>b and a>c:
    print(a,"is the greatest number")
elif b>a and b>c:
    print(b,"is the greatest number")
elif a == b == c:
    print("They are equal")
else:
    print(c,"is the greatest number")