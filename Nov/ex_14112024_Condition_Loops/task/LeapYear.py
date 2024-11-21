"""
the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
"""
try:
    year =int(input("Enter the year : "))

    def leapYear(years):
        if (years % 4 == 0) and (years % 100 != 0):
            print(f"{years} is a leap year")
        elif years % 400 == 0:
            print(f"{years} is a leap year")
        else:
            print(f"{years} is a not leap year")
except:
    print("Enter a valid input: integer!")
else:
    leapYear(year)
