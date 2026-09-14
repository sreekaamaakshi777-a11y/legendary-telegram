#Python code to compare which number is bigger
no1 = int(input("Enter the first number here: "))
no2 = int(input("Enter the second number here: "))

if no1>no2:
    print(no1,"is greator than", no2)
elif no1 == no2:
    print("They are equal")
else:
    print(no2,"is greator than", no1)