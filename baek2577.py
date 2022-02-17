max = 0
num = 0
i = 1
while 1:
    try:
        a = input()
        a = int(a)
        if a>max:
            max = a
            num = i
        i = i + 1
    except EOFError:
        print(max)
        print(num)
        break