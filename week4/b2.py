x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())
Sa = abs((x2-x1)*(y2-y1))
Sb = abs((x4-x3)*(y4-y3))
S = (min(x2, x4) - max(x1,x3))*(min(y4,y2) - max(y1,y3))
# print(Sa,Sb,S)
if S > 0:
    print(Sa + Sb - 2*S)
else :
    print(Sa + Sb)