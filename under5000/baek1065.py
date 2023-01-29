a = input()
a = int(a)
check = 0
for i in range(a):
    
    if (len(str(i+1)) == 1 or len(str(i+1)) == 2):
        check = check+1
    elif(len(str(i+1)) == 3):
        if ((int(str(i+1)[0]) +  int(str(i+1)[2]))/2 == int(str(i+1)[1])):
            check = check+1

print(check)
        