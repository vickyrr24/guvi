nu=int(input())
l=[int(x) for x in input().split()]
sum=0
for i in l:
    sum=sum+i
index=sum//len(l)
print(l[index-1])
