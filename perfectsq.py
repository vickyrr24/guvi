import math
n,m=[int(x) for x in input().split()]
sq=n*m
sqroot=math.sqrt(sq)
if(sq*sq==0 or sqroot*sqroot==sq):
    print("yes")
else:
    print("no")
