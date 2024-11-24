"""
List Methods
append -- adding element in list
extent -- used for adding a list into another
insert -- adding element in list at a particular index
remove -- removing element from list with value or at a particular index
pop -- Remove and return item at index (default last).
sort -- sorting the list in asc order if list is in integer
copy -- copy the list and make a another copy





"""

my_list = [1, 2, 3]

# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append() - # Append object to the end of the list.
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - Append a new list
my_list.extend([7, 8, 10, 9])
print(my_list)

# insert()
my_list.insert(1, "Dutta")
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)

my_list[1] = "Amit"
print(my_list)

# remove()
my_list.remove("Amit")
print(my_list)

print(" --------------------------")
print(" --------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Dutta")
my_list.remove("Dutta")

my_copy_list.sort()

print(my_list)
print(my_copy_list)