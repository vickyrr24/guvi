x,y=input().split()
y=int(y)
x=int(x)
x = x ^ y;
y = x ^ y;
x = x ^ y;
print(x,y)
