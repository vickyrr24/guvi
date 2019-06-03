n=[int(x) for x in input().split()]
mi=n[0]
for i in n:
    if(mi>i):
        mi=i
print(mi)
