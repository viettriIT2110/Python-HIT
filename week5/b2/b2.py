a,b = list(map(int, input().split())),list(map(int, input().split()))
c = { a[i] for i in range(len(a)) if a[i] in b }
print(c)