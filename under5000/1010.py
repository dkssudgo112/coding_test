import sys
sys.setrecursionlimit(100000000)

def facto(p):
    if p == 1 or p == 0:
        return 1

    return facto(p-1) * p

def con(p,q):
    if(q== 0):
        return 1
    if (p == 0):
        return 1
    return int(facto(p) / (facto(q) * facto (p-q)))

def func(p,q):
    if p == q:
        return 1
    if p <= 0:
        return 1
    return func(p-1, q-1) * con(q-p+1,p)


n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(func(a,b))
