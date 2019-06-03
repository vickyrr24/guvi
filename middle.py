number=int(input())
m,n=[int(x) for x in input().split()]
if m<number and number<n:
    print('yes')
else:
    print('no')
