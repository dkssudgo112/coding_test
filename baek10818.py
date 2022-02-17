a = input()
a = int(a)

ls = list(input().split())

max = -1000000
min = 1000000

for i in range(a):
    ls[i] = int(ls[i])
    if ls[i]>max:
        max = ls[i]
    if ls[i]<min:
        min = ls[i]
print(min,max)