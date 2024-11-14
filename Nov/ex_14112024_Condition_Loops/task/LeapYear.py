year =int(input("Enter the year : \n"))

if (year % 4 == 0) and (year % 100 !=0):
    print(f"{year} is a leap year1")
elif year % 400 == 0:
    print(f"{year} is a leap year2")
else:
    print(f"{year} is a not leap year")