case=['even','odd']
n,m=[int(x) for x in input().split()]
print(case[(n+m)%2])
