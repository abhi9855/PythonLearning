# lambda expression
# A lambda is an anonymous function that returns some form of data.


# def add(n):
#     return n + 10
#
# result=lambda n : n + 10
# print(result(10))


def mul(a, b):
    return a * b

result= lambda a,b=10:a * b

print(result(10,2))
