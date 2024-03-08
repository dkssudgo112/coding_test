
dx = [0,1,0,-1]
dy = [-1,0,1,0]

n,m = map(int, input().split())
y,x,dir = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

ans = 0

while(True):

    if board[y][x] == 0:
        ans += 1
        board[y][x] = 2
    cnt = 0
    for i in range(4):
        if 0<=y+dy[i]<n and 0<=x+dx[i]<m:
            if board[y+dy[i]][x+dx[i]] >= 1:
                cnt += 1
        else:
            cnt+=1

    if cnt == 4:
        if 0<=y-dy[dir]<n and 0<=x-dx[dir]<m and board[y-dy[dir]][x-dx[dir]] !=1:

            y = y-dy[dir]
            x = x-dx[dir]
            cnt = 0
            continue
        else:

            break
    else:
        dir = (dir - 1) % 4
        if 0<=y+dy[dir]<n and 0<=x+dx[dir]<m:
            if  board[y+dy[dir]][x+dx[dir]] == 0:
                y = y + dy[dir]
                x = x + dx[dir]
    cnt = 0
print(ans)
    