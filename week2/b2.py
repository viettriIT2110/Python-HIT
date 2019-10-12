
a,b,c = map(int, input().split())
if(a + b > c and a + c > b and b + c > a):
    print("tam giac chắc chắn")
    print("canh dai nhat la : " , max(a,b,c))
    p = (a+b+c)/2
    d = p*2
    print("chu vi la",d)
    print("S = ",math.sqrt(p*(p-a)*(p-b)*(p-c)))
else:
    print("khong phai tam giac")