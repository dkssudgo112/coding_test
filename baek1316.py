a = input()
a= int(a)
check  =0
ans = 0
for i in range(a):
    b = list(input())
    for j in range(len(b)):
        if (j<len(b)-1 and b[j+1] == b[j]):
            b[j] = "?"

        elif (j<len(b)-1 and b[j+1] != b[j]):
            temp = b[j]
            b[j] = "?"
            if(b.count(temp) > 0): check = 1
    
    if (check == 0):
        ans = ans+1
        check = 0
    else:
        check = 0
    
print(ans)
