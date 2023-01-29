a, b = input().split()
a = int(a)
b = int(b)


if b>=45:
    b = b-45
    print(a,b)
else:
    b = 60 + b - 45
    if a>0:
        a= a-1
    else:
        a = 23
    print(a,b)
