a = input()
a = int(a)
for jj in range(a):
    b = list(input().split())

    c = int(b[0])
    d = b[1]

    for i in range(len(d)):
        if (i == len(d)-1):
            for j in range(c-1):
                print(d[i],end='')
            print(d[i])
            continue
        
        for j in range(c):
            print(d[i],end='')