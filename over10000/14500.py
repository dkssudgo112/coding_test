
n, m = map(int, input().split())

MAP = []
for i in range(n):
    MAP.append(list(map(int,input().split())))
visit = [[0]*m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

ans = 0
def DFS(x,y,L,total):
    global ans
    if L== 4:
        ans= max(ans, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                if L==2:
                    visit[nx][ny] = 1
                    DFS(x,y,L+1, total+MAP[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                DFS(nx,ny,L+1,total+MAP[nx][ny])
                visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        DFS(i,j,1,MAP[i][j])
        visit[i][j] = 0
print(ans)    