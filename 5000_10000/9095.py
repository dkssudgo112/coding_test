T = int(input())

li = []
cache = {}


for i in range(T):
    li.append(int(input()))


def solve(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 7
    if n == 7:
        return 44
    if n == 10:
        return 274
    
    if n in cache:
        return cache[n]
    
    result = solve(n-1) + solve(n-2) + solve(n-3)
    cache[n] = result
    return result

for i in range(T):
    print(solve(li[i]))