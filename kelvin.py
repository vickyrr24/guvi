class convert:
    def __init__(self,cel):
        self.celi=cel
    def cel(self):
        return(self.celi+273)
n=int(input())
obj=convert(n)
print(obj.cel())
