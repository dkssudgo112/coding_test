from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]

print(board)
k  = int (input())

MAP = []

for i in range(k):
    MAP.append(list(map(int,input().split())))

print(MAP)
for i in range(len(MAP)):

    board[MAP[i][0]-1][MAP[i][1]-1] = 2

l = int(input())

MOVE = {}
for i in range(l):
    a, b = map(str,input().split())
    MOVE[int(a)] = b


def move(dir):
    if dir == 0:
        return 0,1
    elif dir == 1:
        return 1,0
    elif dir == 2:
        return  0,-1
    else:
        return  -1,0

ans = 0


snake = deque()
snake.append([0,0])
dir = 0

board[0][0] = 1
x = [0,0]

while(True):
    print(snake)
    print(board) 
    print( "ans : "+ str(ans))
    print ("dir : " + str(dir))
    dx, dy = move(dir)
    print(x)
    if (x[0]+dx) < 0 or x[0]+dx >= n or x[1] + dy <0 or x[1]+ dy >=n:
        print(ans)
        break
    
    x[0] += dx
    x[1] += dy
    if board[x[0]][x[1]] == 2:
        snake.append([x[0],x[1]])
        board[x[0]][x[1]] = 1
        if (ans in MOVE):
            print("turn")
            change = MOVE[ans]
            if change == 'L':
                dir = (dir  + 1) % 4 
            else:
                dir = (dir - 1) % 4         

        ans = ans + 1
        continue
    elif board[x[0]][x[1]] == 0:
        board[x[0]][x[1]] = 1
        snake.append([x[0],x[1]])
        tx= snake.popleft()
        board[tx[0]][tx[1]] = 0

        if (ans in MOVE):
            print("turn")
            change = MOVE[ans]
            if change == 'D':
                dir = (dir  + 1) % 4 
            else:
                dir = (dir - 1) % 4 
        ans = ans + 1
        continue

    elif board[x[0]][x[1]] == 1:
        print(ans)
        break


