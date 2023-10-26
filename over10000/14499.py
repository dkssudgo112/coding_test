

n, m, y, x, k = map(int, input().split())
MAP = []

for i in range(n):
    MAP.append(list(map(int,input().split())))

oper = list(map(int, input().split()))

#print(MAP)
#print(x,y)
#print(oper)

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
def move(dir):
    if dir == 1:
        return 0,1
    elif dir == 2:
        return 0,-1
    elif dir == 3:
        return -1,0
    else:
        return 1,0

dice = [0, 0, 0, 0, 0, 0] 
def turn(dir):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


dir = 0
'''
if MAP[y][x] == 0:
    MAP[y][x] = dice[5]
else:
    dice[5] = MAP[y][x]
    MAP[y][x] = 0
'''
for i in range(k):
    dir = oper[i]
    dy, dx = move(dir)
    if x+dx < 0 or x+dx >=m or y+dy <0 or y+dy >= n:
        continue
    x = x+dx
    y = y+dy
    turn(dir)
    if MAP[y][x] == 0:
        MAP[y][x] = dice[5]
    else:
        dice[5] = MAP[y][x]
        MAP[y][x] = 0
    print(dice[0])

