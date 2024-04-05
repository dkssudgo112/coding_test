n = int(input())

MAP = [list(map(int, input())) for _ in range(n)]

def check_all_same(size, x,y):
    
    check = MAP[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if MAP[i][j] != check:
                check = -1
                break
    
    if check == -1:
        print("(", end='')
        size = size // 2
        check_all_same(size, x, y)
        check_all_same(size, x, y + size)
        check_all_same(size, x + size, y)
        check_all_same(size, x + size, y + size)
        print(")", end='')
    else:
        print(check, end='')

check_all_same(n,0,0)