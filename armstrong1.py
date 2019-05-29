n,m=input().split()
n=int(n)
m=int(m)
def arm(a):
    sum=0
    temp=a
    while(a>0):
            t=a%10
            sum=sum+t**3
            a=a//10

    if(sum==temp):
            return 1
    else:
            return 0
for i in range(n+1,m):
    if(arm(i)):
        print(i,end=" ")
