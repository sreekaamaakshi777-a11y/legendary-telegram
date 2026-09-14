age = int(input("Enter age here: "))

if age<2:
    print("Infant")
elif age<4:
    print("Toddler")
elif age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age>60:
    print("Senior citizen")
else:
    print("Adult")
        