a, b = input().split()
a = int(a)
b= int(b)

c = input()
c = int(c)

ti = a*60 + b

ti = ti + c

b = ti % 60
a = int(ti / 60) % 24

print(a,b)