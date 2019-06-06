import re
n=input()
h=re.findall('\d+',n)
print(*h)
