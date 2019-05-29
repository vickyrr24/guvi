a=int(input())
sum=0
temp=a
while(a>0):
	t=a%10
	sum=sum+t**3
	a=a//10

if(sum==temp):
	print("yes")
else:
	print("no")
