a = input()
b = input()

a = int(a)
b = int(b)

print(a*(b%10))
print(a*int((((b%100)-(b%10))/10)))
print(a*int(b/100))
print(a*b)
