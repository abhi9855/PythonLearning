# Fibonacci Series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

first = 0
second = 1
next = 1

count=int(input("Enter the no. to find the Fibonacci Series : "))

if count>0:
    print(f"Fibonacci Series for first {count} no. is: ",end="")
    while count>=1:
        print(f"{first}",end=" ")

        next = first + second
        first = second
        second = next

        count-=1
else:
    print("Count less than 1, Please five a no. greater than 1")

