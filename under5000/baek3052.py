s = set()

for i in range(10):
    a = input()
    a = int(a)

    s.add(a%42)

print(len(s))
