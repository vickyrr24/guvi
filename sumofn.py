class sumof:
    def __init__(self,n,l):
        self.n=n
        self.l=l
    def sum(self):
        su=0
        for i in range(0,self.n):
            su=su+l[i]
        print(su)
n=int(input())
l=[int(x) for x in input().split()]
obj=sumof(n,l)
obj.sum()
