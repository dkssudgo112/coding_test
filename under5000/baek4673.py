A= []
for i in range(10000):
    i = i+1
    A.append(i)
for a in range(10000):
    i=a+1
    self_num = []
    final_self_num = i
    st_i = str(i)
    for c in range(len(st_i)):
        final_self_num = final_self_num + int(st_i[c])
       # print(final_self_num)
    a = a+1
    
    if final_self_num in A:
        A.remove(final_self_num)
    #print(a)
#print(A)

for a in range(len(A)):
    print(A[a]) 

