a = input()
a= int(a)
num = 0
temp = a

while 1:
    
    a=(a%10)*10 +(int(a/10) + a%10)%10
    
    num = num +1

    if temp == a:
        print(num)
        break