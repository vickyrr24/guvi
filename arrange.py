vi=int(input())
lst=[int(x) for x in input().split()]
for i in range(0,len(lst)-1):
    if lst[i]>lst[i+1]:
        print(i)
