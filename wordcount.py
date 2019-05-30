st=input()
count=0
for i in range(1,len(st)):
    if(st[i-1]!=" " and st[i]==" "):
        count=count+1
    if(i==len(st)-1):
        count=count+1
print(count)
