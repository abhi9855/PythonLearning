# Write a Python program to find the factorial of a number

def factorial(n):
    fact=1
    if n<0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n==0 or n==1:
        return fact
    else:
        for i in range(2,n+1):
            fact=fact*i
        return fact


num=int(input("Enter the no. you want factorial : "))
result=factorial(num)
print(f"Factorial of {num} is {result}")