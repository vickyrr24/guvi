string=input()
string=set(string)
check=['0','1']
f=0
for i in string:
    if(i not in check):
        print("no")
        f=1
        break
if f==0:
    print("yes")
