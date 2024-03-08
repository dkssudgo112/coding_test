a = list(input().split())
b = []
c = [1,1,2,2,2,8]
for i in range(len(a)):
    b.append(c[i]-int(a[i]))

print(*b)


