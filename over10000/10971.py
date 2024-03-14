N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited_list = []

min_dist = 9999999

def solve(start,dist):
    global min_dist
    if len(visited_list) == N:
        if (W[start][visited_list[0]] == 0):
            return 
        dist += W[start][visited_list[0]]
        min_dist = min(min_dist, dist)
        return
    
    for i in range(N):
        if i not in visited_list and W[start][i] != 0:
            visited_list.append(i)
            dist += W[start][i]
            if (dist > min_dist):
                visited_list.pop()
                dist -= W[start][i]
                continue
            solve(i,dist)
            visited_list.pop()
            dist -= W[start][i]

for i in range(N):
    visited_list.append(i)
    solve(i, 0)
    visited_list.pop()

print(min_dist)