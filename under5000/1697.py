
q= 0
def find_min_time(n, k):
    global q
    if n == k:
        return
    if n > k:
        q += n-k
        return
    if k % 2 == 0:
        q += 1
        find_min_time(n, k//2)
    else:
        q += 1
        find_min_time(n, k+1)
        q += 1
        find_min_time(n, k-1)
    

if "__main__" == __name__:
    a,b = input().split()
    a = int(a)
    b = int(b)  
    print(a+b)

    find_min_time(a, b)
    print(q)

