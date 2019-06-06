def gcd(a,b): 
	if (b == 0): 
		return a 
	return gcd(b, a%b) 
n,m=[int(x) for x in input().split()]
print(n*m//gcd(n,m))
