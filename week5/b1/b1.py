a,b = list(map(int, input().split())),list(map(int, input().split()))
print ([ a[i] + b[i] for i in range(len(a)) ])