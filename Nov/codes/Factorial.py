# Python 3 program to find
# factorial of given number

# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 4! -> 4*3*2*1 -> 24
# 3! -> 3*2*1 -> 6


def factorial(num):

    fact= 1
    if num>0:
        for i in range (2, num+1):
            fact*=i
        return fact
    else:
        print("You have entered no. less than zero! Please give no. greater than 1")

num = int(input("Enter the no. you want to find factorial : "))
print(f"Factorial of {num} is {factorial(num)}")