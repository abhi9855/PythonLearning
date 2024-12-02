# Write a Python program that takes two lists and returns True if they have at least one common member.

list1 = [10, 8, 9, 1, 2]
list2 = [4, 3, 5, 6, 7, 1]
result = False


def compareTwoList(a, b):
    for x in list1:
        for y in list2:
            if x == y:
                # print(x,y)
                result = True
    return result


output = compareTwoList(list1, list2)
print(output)
