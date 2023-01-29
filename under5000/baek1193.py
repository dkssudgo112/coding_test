a = input()
a = int(a)

#a(n) - a(n-1) = n
#a(n) = n(n+1)/2
n = 0

while(True):
    b = int(n* (n+1) / 2)
    n = n+1
    c= int(n* (n+1) / 2)
    if(a>b and a<=c and n%2 == 0):
        print(a - int(n* (n-1) / 2), end='')
        print('/',end='')
        print(n - (a - int(n* (n-1) / 2))+1, end='')
        break
    elif(a>b and a<=c and n%2 == 1):
        print(n - (a - int(n* (n-1) / 2))+1, end='')    
        print('/',end='')
        print(a - int(n* (n-1) / 2), end='')
        break
    