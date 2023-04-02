
n = int(input())
min = -1
cal = 0

def cal_min(n,cal):
    a = int(n / 5)
    b = n % 5
    global min

    if b == 1 or b == 2 or b== 4:
        if a >= 1:
            cal = cal+1
            cal_min(n-3,cal)

    elif b == 0:
        if min >= a+ cal or min == -1:
            min = a + cal
    else:
        if min >= a+ cal+1 or min == -1:
            min = a+1+cal


cal_min(n,cal)
print(min)