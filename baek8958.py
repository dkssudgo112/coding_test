a = input()
a = int(a)
c = 0
d = 0

for i in range(a):
    b = input()
    for j in range(len(b)):
        if(b[j] == 'O'):
            c = c+1
            
            d = d+c
        else:
            c = 0
    print(d)
    d = 0
    c= 0