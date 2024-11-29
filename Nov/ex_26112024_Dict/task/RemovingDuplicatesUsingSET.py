# Question 2 :
# my_list = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates from a list using a set.
# Output: [1, 2, 3, 4, 5]


def removeDuplicatesFromList(my_list):
    print("The list before removing duplicates :", my_list)
    result = list()
    for item in my_list:
        if item not in result:
            result.append(item)
    return result


my_list = [1, 2, 2, 3, 4, 4, 5]
result=removeDuplicatesFromList(my_list)
print("The list after removing duplicates :", result)