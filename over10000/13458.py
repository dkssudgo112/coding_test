
n = int(input())

m = list(map(int,input().split()))

p = list(map(int,input().split()))

ans = 0

def bugam(a,b):
    if a<=0:
        return 0
    if not a%b == 0:
        return int(a/b) + 1
    else:
        return int(a/b)


for i in range(len(m)):
    ans += 1 + bugam(m[i]-p[0],p[1])


print(int(ans))