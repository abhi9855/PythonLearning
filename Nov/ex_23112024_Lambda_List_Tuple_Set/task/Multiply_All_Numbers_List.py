# Write a Python program to multiply all numbers in a list.

def multiplyAllItem():
    for i in range (1,n+1):
        my_list.append(int(input(f"Enter {i} no to store in list : ")))

    result=1

    for item in my_list:
        result=result*item
    return result

n=int(input("Enter the size of list : "))
# my_list = [10, 8, 9, 1, 2]
my_list=list()

my_result=multiplyAllItem()
print(f"Multiply of total no. of items {my_list} :",my_result)