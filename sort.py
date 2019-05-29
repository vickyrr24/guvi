n=int(input())
l=[int(x) for x in input().split()]
for i in range(0,n):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
for i in l:
    print(i,end=" ")
