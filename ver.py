class reverse:
    def __init__(self,a):
        self.a=a
    def cal(self):
        reverse=self.a[::-1]
        return(reverse)
        
x=input()
obj=reverse(x)
print(obj.cal())
