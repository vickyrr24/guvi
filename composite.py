a=int(input())
flag=0
for i in range(2,a//2+1):
	if(a%i==0):
		flag=flag+1
if(flag<=0):
	print("no")
else:
	print("yes")
