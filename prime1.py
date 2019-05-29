n,m=input().split()
n=int(n)
m=int(m)
def prime(a):
	if(a==1):
		return("No")
	flag=0
	for i in range(2,a//2+1):
		if(a%i==0):
			flag=1
	if(flag==0):
		return("Yes")
	else:
		return("No")

for i in range(n+1,m):
	test=prime(i)
	if(test=="Yes"):
		print(i,end=" ")
