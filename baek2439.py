a = input()
a= int(a)
n = a-1

for i in range(a):
    i = i+1
    for j in range(a):
        if(j<n):
            print(" ",end='')
        else:
            print("*",end='')
    n = n-1
    print("")
