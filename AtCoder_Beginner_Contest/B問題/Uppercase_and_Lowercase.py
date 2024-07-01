S = input()
if len(S) == 1:
    print(S)

up = 0
low = 0
if len(S) >= 2:
    for i in S:
        if i.isupper():
            up += 1
        if i.islower():
            low += 1

    if up > low:
        print(S.upper())
    if low > up:
        print(S.lower())