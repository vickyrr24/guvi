n=input()
a,b=0,0
for x in n:
    if x.isnumeric() and a==0:
        a=a+1
    if(x.isalpha() and b==0):
        b=b+1
if(a==1 and b==1):
    print("Yes")
else:
    print("No")
