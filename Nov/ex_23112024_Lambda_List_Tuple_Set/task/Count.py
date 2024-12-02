""" Write a Python program to count the number of strings in a list
    where the string length is 2 or more and the first and last characters are the same.
"""


def match_words():
    count = 0
    for item in myList:
        if len(item) > 1 and item[0] == item[-1]:
            count += 1

    return count


myList = ['abc', 'xyz', 'aba', '1221']
output = match_words()
print(output)
