a, b = input().split()
a= int(a)
b= int(b)
start = 0

s = list(input().split())
for i in range(a):
    s[i] = int(s[i])
    if s[i]<b:
        if start==0:
            print(s[i],end='')
            start = 1
        else:
            print(" ",end='')
            print(s[i],end='')




