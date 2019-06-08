class ap:
    def __init__(self,a,d,n):
        self.a=a
        self.d=d
        self.n=n
    def cal(self):
        ap=self.n//2*(2*self.a+(self.n-1)*self.d)
        return ap
a,b,c=[int(x) for x in input().split()]
obj=ap(a,b,c)
print(obj.cal())
