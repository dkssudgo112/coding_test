

n,m,h = map(int, input().split())

left_set = set()

for i in range(m):
    a,b = map(int,input().split())
    left_set.add((a,b))

ans = 9999

def where_endpoint(x,y):
    global h    
    if y > h:
        return x
    
    if (x,y) in left_set:
        return where_endpoint(x+1, y+1)
    elif (x-1, y) in left_set:
        return where_endpoint(x-1,y+1)
    else:
        return where_endpoint(x,y+1)

answer_set = set()

def let_go(cnt):
    global ans
    if cnt > 3:
        answer_set.add(9999)
        return
    if cnt >= ans:
        return
    check = 9999
    for i in range(1, n+1):
        if where_endpoint(i, 1) != i:
            check = -9999
            break
    if check == 9999:
        answer_set.add(cnt)
        if (ans > cnt):
            ans = cnt
        return cnt
    
    else:
        for i in range(1, n+1):
            for j in range(1, h+1):
                if (i,j) not in left_set and (i-1,j) not in left_set:
                    left_set.add((i,j))
                    a = let_go(cnt+1)
                    left_set.remove((i,j))
                    if a == 1:
                        return


let_go(0)

if min(answer_set) ==9999:
    print(-1)
else:
    print(min(answer_set))