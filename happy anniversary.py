#happy anniversary
MONTHS_IN_YEAR = 12

def happy_anniversary():
    name = input("Name: ")
    month = input("Month: ")
    date = input("Date: ")
    year = input("Year: ")
    
    print(name, "Your anniversary is on ", date, "th ", month, ",", year, "!")

def main():
    happy_anniversary()
    
main()