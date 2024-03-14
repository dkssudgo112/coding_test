n = int(input())
A = list(map(int, input().split()))
visited = [0 for i in range(n)]


def dist(A, n):
    ret = 0
    for i in range(n-1):
        ret += abs(A[i]-A[i+1])
    return ret

A_list = []
max_ret = 0


def solve(A_list):
    if len(A_list) == n:
        global max_ret
        max_ret = max(dist(A_list, n), max_ret)

        return
    
    for i in range(n):
        if visited[i] == 0:
            A_list.append(A[i])
            visited[i] = 1
            solve(A_list)
            A_list.pop()
            visited[i] = 0

solve(A_list)
print(max_ret)
