import re
n=input()
h=re.findall('\d+',n)
for i in h:
    print(i,end="")

