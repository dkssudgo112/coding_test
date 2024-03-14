N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]


def what_is_color(n, start_x, start_y):
    if n==1:
        return MAP[start_y][start_x]
    temp = MAP[start_y][start_x]

    for j in range(n):
        for i in range(n):
            if MAP[start_y+j][start_x+i] != temp:
                return 2
    return temp

black = 0
white = 0

def count(n,x,y):
    global black
    global white
    if what_is_color(n,x,y)==0 or what_is_color(n,x,y) == 1:
        if MAP[y][x] == 1:
            black += 1
        else:
            white += 1
        return

    count(n//2,x,y)
    count(n//2,x+n//2, y+n//2)
    count(n//2,x, y+n//2)
    count(n//2,x+n//2, y)



count(N,0,0)
print(white)
print(black)