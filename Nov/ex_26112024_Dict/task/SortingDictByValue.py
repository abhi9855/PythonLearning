# Sort a dictionary by its values in descending order
d = {"a": 3, "b": 1, "c": 2}

print("Dictionary", d)

# Sorting and printing dictionary keys
for i in sorted(d.items()):
    print(i, end=" ")
print()

# Initializing the key-value pairs
# d = {2: 56, 100: 2, 3: 323}

print("Dictionary", d)

# Sorting key-value pairs by value, and by key if values are the same
sorted_items = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))

print(sorted_items)