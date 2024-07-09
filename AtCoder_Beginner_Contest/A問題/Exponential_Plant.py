H = int(input())
plant = 0
day = 0
while True:
    plant = plant+2**day
    if plant > H:
        print(day+1)
        break
    day += 1