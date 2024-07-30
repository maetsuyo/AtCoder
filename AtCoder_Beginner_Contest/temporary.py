# for i in range(3):
#     new_name = "temp_" + str(i)
#     globals()[new_name] = i*5

# print(type(temp_1))

dict = {}

for i in range(1, 5):
    dict[i] = 0
    dict[i] = dict[i]+1

print(dict)