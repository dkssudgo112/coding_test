def floor(k,n):
    if k == 0:
        return n
    if n == 1:
        return floor(k-1,n)
    num = 0
    for i in range(n):
        i = i+1
        num = num + floor(k-1,i)
    return num

t = int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    print(floor(a,b))