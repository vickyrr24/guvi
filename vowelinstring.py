n=input()
f=0
lst=['A', 'E', 'I', 'O', 'U','a','e','i','o','u']
for x in n:
    if(x in lst):
        f=1
        break
if(f):
    print("yes")
else:
    print("no")
