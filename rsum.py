n,m=input().split()
n=int(n)
m=int(m)
sum=0
l=[int(x) for x in input().split()]
for i in range(0,m):
    sum=sum+l[i]
print(sum)
