class mod:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def cal(self):
        print(int((x*y)%z))
        
x,y,z=map(int,input().split())
obj=mod(x,y,z)
obj.cal()
