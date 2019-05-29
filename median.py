n=int(input())
l=[int(x) for x in input().split()]
l.sort()
index=int((n-1)//2)
print(l[index])
