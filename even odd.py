#Even number or odd number
num = int(input("Enter number here: "))

if num == 0:
    print("Zero is neither odd not even")
elif num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")