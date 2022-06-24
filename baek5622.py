a = input()
ans = 0

for i in range(len(a)):
    if (a[i] == 'A' or a[i] == 'B' or a[i] == 'C' ):
        ans = ans + 3
    elif (a[i] == 'D' or a[i] == 'E' or a[i] == 'F' ):
        ans = ans + 4
    elif (a[i] == 'G' or a[i] == 'H' or a[i] == 'I' ):
        ans = ans + 5
    elif (a[i] == 'J' or a[i] == 'K' or a[i] == 'L' ):
        ans = ans + 6
    elif (a[i] == 'M' or a[i] == 'N' or a[i] == 'O' ):
        ans = ans + 7
    elif (a[i] == 'P' or a[i] == 'Q' or a[i] == 'R' or a[i] == 'S' ):
        ans = ans + 8
    elif (a[i] == 'T' or a[i] == 'U' or a[i] == 'V' ):
        ans = ans + 9
    elif (a[i] == 'W' or a[i] == 'X' or a[i] == 'Y' or a[i] == 'Z' ):
        ans = ans + 10
print(ans)