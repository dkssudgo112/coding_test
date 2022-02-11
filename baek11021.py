import sys

x = sys.stdin.readline()
x = int(x)


for i in range(x):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print("Case #%d: %d" %(i+1,a+b))
