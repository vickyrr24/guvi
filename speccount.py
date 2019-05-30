n=input()
count=0
for i in n:
    if(not(ord(i)>=48 and ord(i)<=57 or ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or i==" ")):
        count=count+1
print(count)
