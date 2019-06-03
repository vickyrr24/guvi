inp=int(input())
flag=0
for i in range(2,inp//2+1):
	if(inp%i==0):
		flag=flag+1
if(flag<=0):
	print("yes")
else:
	print("no")
