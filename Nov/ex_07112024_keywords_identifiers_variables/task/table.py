"""

Take a input from a user and print the table
n = 2 & print
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
"""

num=int(input("Enter the no. you want table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")