num1=int(input("Enter the no. you want table: "))
num2=int(input("Enter the no. you want table: "))

# num1=-5;
# num2=10

print(f"Before swaping num1: {num1}, num2: {num2}")

num1=num1+num2
num2=num1-num2
num1=num1-num2

print(f"After swaping num1: {num1}, num2: {num2}")