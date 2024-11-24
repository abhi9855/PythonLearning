#Lambda

# def triple_me(num):
#     return num**3
#
# result_l= triple_me(2)
# print(result_l)

result_l=lambda  num=2:num ** 3
print(result_l(2))