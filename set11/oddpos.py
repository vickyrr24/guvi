n,m=map(int,input().split())
lst=[int(x) for x in input().split() if int(x)%2!=0]
print(lst[m-1])
