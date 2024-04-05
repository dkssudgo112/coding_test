n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

count__1 = 0
count_0 = 0
count_1 = 0

def check_all_same(x,y,n):
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y, y+n):
            if check != graph[i][j]:
                check = -9999
                break
    global count_0
    global count_1
    global count__1
    if check == -9999:
        n = n // 3
        check_all_same(x,y,n)
        check_all_same(x+n,y+n,n)
        check_all_same(x+2*n,y+2*n,n)

        check_all_same(x+n,y,n)
        check_all_same(x,y+n,n)
        check_all_same(x+2*n,y+n,n)

        check_all_same(x+n,y+2*n,n)
        check_all_same(x,y+2*n,n)
        check_all_same(x+2*n,y,n)


    elif check == -1:
        count__1 += 1
    elif check == 0:
        count_0 += 1
    else:
        count_1 += 1
    

 
check_all_same(0,0,n)

print(count__1)
print(count_0)
print(count_1)