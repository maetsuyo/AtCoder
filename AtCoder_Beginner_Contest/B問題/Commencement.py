S = input()
S = list(S)
new_S = set(list(S))

count_dict = {}
for i in range(1, 51):
    count_dict[i] = 0

for j in new_S:
    count = S.count(j)
    count_dict[count] += 1

answer = "Yes"
for value in count_dict.values():
    if value != 0 and value != 2:
        answer = "No"
        break

print(answer)