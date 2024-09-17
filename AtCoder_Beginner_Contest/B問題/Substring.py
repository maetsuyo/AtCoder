S = input()

substring_list = []
count = 0
for i in range(1, len(S)+1):
    for j in range(1, len(S)+1):
        if len(S)+1>=j+i and S[j-1:j-1+i] not in substring_list:
            substring_list.append(S[j-1:j-1+i])
            count += 1

print(count)