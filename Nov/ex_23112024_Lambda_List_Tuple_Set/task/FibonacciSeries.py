# Write a Python program to get the Fibonacci series between 0 to 5
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
n = 50
n = int(input("Enter the no. to find the Fibonacci Series : "))
first = 0
second = 1
third = 1
if n > 0:
    print(f"Fibonacci Series for first {n} no. is: ", end="")
    for i in range(1, n + 1):
        print(first, end=' ')
        third = first + second
        first = second
        second = third
else:
    print("Count less than 1, Please give a no. greater than 1")
