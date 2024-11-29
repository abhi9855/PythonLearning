str="geeksforgeeks"

vowel=['a','e','i','o','u']
count=0
result=dict()

def vowelCount(str):
    for char in str:
        if char in vowel:
            if char !=' ':
                result[char]=result.get(char, 0)+1
    return result

output=vowelCount(str)
print(output)

for key,value in output.items():
    print(key, " -> ", value)

