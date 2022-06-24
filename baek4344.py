a = input()
a = int(a)

for i in range(a):
    num_list = list(map(int, input().split()))
    avg = sum(num_list[1:],0.0) / (len(num_list) - 1)
    c = 0
    for j in range(len(num_list)-1):
        if(num_list[j+1]>avg): c = c+1
    print("{:.3f}%".format(round(c/(len(num_list)-1)*100,3)))