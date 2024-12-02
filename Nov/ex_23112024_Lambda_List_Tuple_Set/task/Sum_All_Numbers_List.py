# Write a Python program to sum all numbers in a list.

my_list = [10,8,9,1,2]

def sumAllNo(list):
    result = 0
    for item in my_list:
        result+=item
    return result

output = sumAllNo(my_list)
print(f"Sum of total no. of items {my_list} : {output}")