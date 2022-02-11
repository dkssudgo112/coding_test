a = input()
b = input()

a = int(a)
b = int(b)

if a>0 and b>0:
    print("1")
if a>0 and b<0:
    print("4")
if a<0 and b>0:
    print("2")
if a<0 and b<0:
    print("3")