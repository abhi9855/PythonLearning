try:
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    num3 = int(input("Enter the num3: "))

    def sumOfThreeNum(num1=100,num2=100,num3=100):
        return num1+num2+num3

    result = sumOfThreeNum(num1, num2, num3)
    result2 = sumOfThreeNum()
    result2 = sumOfThreeNum(10)
    result2 = sumOfThreeNum(10, num3=20)

except:
    print("Enter the valid input: Integer")
else:
    print(f"The sum of {num1},{num2},{num3} : {result}")

"""
#result2 = sumOfThreeNum(10,20,30)
print(result2)
"""