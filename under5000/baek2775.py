test_case = input()
tc = int(test_case)
for i in range(tc):
    flr = int(input())
    ho = int(input())
    hlo = 0 
    hllo = 1
    no=0
    if flr ==1: 
        for a in range (1,ho+1):
             hlo = hlo + a
    elif flr >1: 
        for a in range (1,ho+1):
             hlo = hlo + a
        hlo = hlo + ho*(flr) -flr
    #print(hlo)
    for i in range(flr,flr + ho):
        hllo = hllo + i
    print(hllo)

