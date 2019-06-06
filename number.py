import re
n=input()
h=re.findall('\d+',n)
if(h==[]):
    print()
else:
    for i in h:
        print(i,end="")

