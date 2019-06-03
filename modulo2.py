n,m=[int(x) for x in input().split()]
lst=["yes","no"]
print(lst[abs(n-m)%2])
