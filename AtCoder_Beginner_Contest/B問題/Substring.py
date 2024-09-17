S = input()

for i in range(1, len(S)+1):
    for j in range(1, len(S)+1):
        if len(S)+1 >= j+i:
            print(S[j-1:j-1+i])

    print("-")