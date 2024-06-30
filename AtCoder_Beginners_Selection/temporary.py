bool = False
answer = "NO"
S = input()
T = ""
words = ["dream", "dreamer", "erase", "eraser"]
for i in words:
    T += i
    if T in S:
        if S == T:
            answer = "YES"
            bool = True
            break
        else:
            for j in words:
                temp = T
                T += j
                if S == T:
                    answer = "YES"
                    bool = True
                    break
                else:
                    T = temp
            T = ""
            if bool == True:
                break 
    else:
        T = ""

print(answer)