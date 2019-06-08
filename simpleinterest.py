class interest:
    def __init__(self,p,n,r):
        self.p=p
        self.n=n
        self.r=r
    def calc(self):
        return(self.p*self.n*self.r//100)
p,n,r=[int(x) for x in input().split()]
obj=interest(p,n,r)
print(obj.calc())
