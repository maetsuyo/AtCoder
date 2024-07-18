S = input()
T = input()

number_list = []
if S == T:
    for i in range(len(S)):
        number_list.append(i+1)

if S != T:
    index = 0
    for j in range(len(S)):
        for k in range(index, len(T)):
            if S[j] == T[k]:
                number_list.append(k+1)
                index = k+1
                break

print(*number_list)