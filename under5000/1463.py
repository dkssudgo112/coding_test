

n = int(input())

cache = {}


def solve(n, cnt):
    if n <= 1:
        return cnt
    
    if (n, cnt) in cache:
        return cache[(n, cnt)] 

    if n % 3 != 0 and n % 2 != 0:
        result = solve(n-1, cnt+1)
        cache[(n, cnt)] = result
        return result

    if n % 3 != 0 and n % 2 == 0:
        result = min(solve(n-1,cnt+1), solve(n//2, cnt+1))
        cache[(n, cnt)] = result
        return result
    
    if n %3 ==0 and n%2 != 0:
        result = min(solve(n-1,cnt+1), solve(n//3, cnt+1))
        cache[(n, cnt)] = result
        return result
    
    result = min( solve(n//3, cnt+1), solve(n//2, cnt+1))
    cache[(n, cnt)] = result
    return result

print(solve(n,0))

