a = input()
a = int(a)
n = 0

#1, 6, 12, 18
# a(n+1) - a(n) = 6n
# a(n+1) = 3n(n+1) + 1


while(True):
    if(a == 1):
        print("1")
        break
    b = 3*n*(n+1) + 1
    n = n+1
    c = 3*n*(n+1) + 1
    if(a>=b and a<=c):
        print(n+1)
        break
