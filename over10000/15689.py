
n, m = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cctv_mode = [[],[[0],[1],[2],[3]], [[0,2],[1,3]], [[0,1],[1,2],[2,3],[3,0]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]

cctv_list = []


for i in range(n):
    for j in range(m):
        if 1<=board[i][j]<=5:
            cctv_list.append([board[i][j],j,i])



def fill(dir_list, board, x,y):
    for i in dir_list:
        nx = x
        ny = y
        while(True):
            
            nx += dx[i]
            ny += dy[i]
            if not( 0<=nx<m and 0<=ny<n):
                break
            if(board[ny][nx]==6):
                break
            if(board[ny][nx] == 0):
                board[ny][nx] = -1
              
ans = 1e9

import copy

def DFS(board, depth):
    global ans
    if depth == len(cctv_list):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    cnt += 1
        ans = min (ans, cnt)
        return
    
    temp_board = copy.deepcopy(board)

    cctv = cctv_list[depth]
    for i in cctv_mode[cctv[0]]:
        fill(i,temp_board ,cctv[1],cctv[2])
        DFS(temp_board, depth+1)
        temp_board = copy.deepcopy(board)

DFS(board, 0)
print(ans)