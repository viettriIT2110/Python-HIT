n, arr = int(input()), {}
for i in range(n):
    s = input()
    arr[s] = (1 if s not in arr else arr[s]+1)
Max = 0
nho = ' '
for key in arr:
    if Max < arr[key]:
        Max = arr[key]
        nho = key
print("Tên người giải được nhiều câu đố nhất là: ", nho)
