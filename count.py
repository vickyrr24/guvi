n,k=[int(x) for x in input().split()]
li=[int(x) for x in input().split()]
count=0
for i in range(n):
    if(li[i]==k):
        count+=1
print(count)
