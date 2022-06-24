a = input()

ans = 0

ans = ans - a.count("c=") - a.count("c-") - a.count("dz=") - a.count("d-") - a.count("lj") - a.count("nj") - a.count("s=") - a.count("z=")


ans = ans + len(a)

print(ans)
