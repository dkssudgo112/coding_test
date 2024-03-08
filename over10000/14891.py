
q_list =[]

for i in range(4):
    q_list.append(str(input()))

from copy import deepcopy
from collections import deque
que1 = deque()
que2 = deque()
que3 = deque()
que4 = deque()
for i in range(8):
    que1.append(int(q_list[0][i]))
    que2.append(int(q_list[1][i]))
    que3.append(int(q_list[2][i]))
    que4.append(int(q_list[3][i]))

k = int(input())

turn_list = []
for i in range(k):
    turn_list.append(list(map(int,input().split())))



def turn(q,dir):
    if dir == -1:
        temp = q.popleft()
        q.append(temp)
    else:
        temp = q.pop()
        q.appendleft(temp)


for i in range(k):
    if turn_list[i][0] == 1:
        dir = turn_list[i][1]
        if que1[2] != que2[6]:
            if que2[2] != que3[6]:
                if que3[2] != que4[6]:
                    turn(que4, -1 * dir)
                turn(que3, dir)
            turn(que2, -1 * dir)
        turn(que1, dir)
    elif turn_list[i][0] == 2:
        dir = turn_list[i][1]
        
        if que1[2] != que2[6]:
            turn(que1, -1 * dir)
        if que2[2] != que3[6]:
            if que3[2] != que4[6]:
                turn(que4,dir)
            turn(que3,-1 * dir)
        turn(que2,dir)
    elif turn_list[i][0] == 3:
        dir = turn_list[i][1]
        
        if que3[2] != que4[6]:
            turn(que4, -1 * dir)
        if que2[2] != que3[6]:
            if que1[2] != que2[6]:
                turn(que1,dir)
            turn(que2,-1 * dir)
        turn(que3,dir)
    else:
        dir = turn_list[i][1]
        if que3[2] != que4[6]:
            if que2[2] != que3[6]:
                if que1[2] != que2[6]:
                    turn(que1, -1 * dir)
                turn(que2, dir)
            turn(que3, -1 * dir)
        turn(que4, dir)


ans = 0
if que1[0] == 1:
    ans += 1
if que2[0] == 1:
    ans += 2
if que3[0] == 1:
    ans += 4
if que4[0] == 1:
    ans += 8

print(ans)