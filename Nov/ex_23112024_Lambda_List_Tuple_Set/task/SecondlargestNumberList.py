# my_list = [10,8,9,1,2]
# Output: [1, 2, 8, 9, 10]

my_list=list()
# my_list = [10,8,9,1,2]
items=int(input("Enter the total no. of elements in list : "))
i=1
while i<items+1:
    a=int(input(f"enter the {i}st element:"))
    my_list.append(a)
    i+=1
my_list.sort()
print("Sorted list :",my_list)
print("2nd largest no. in list is  :",my_list[-2])
print("2nd smallest no. in list is  :",my_list[1])
