# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

try:
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    num3 = int(input("Enter the num3: "))

    def sumOfThreeNum(num1=100,num2=200,num3=300):
        return num1+num2+num3

    result = sumOfThreeNum(num1, num2, num3)
    result2 = sumOfThreeNum()
    result2 = sumOfThreeNum(10)
    result2 = sumOfThreeNum(10, num3=20)

except:
    print("Enter the valid input: Integer")
else:
    print(f"The sum of {num1},{num2},{num3} : {result}")


# result2 = sumOfThreeNum(10, num3=20)
# print(result2)
