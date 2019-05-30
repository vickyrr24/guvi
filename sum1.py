lst=int(input())
su=0
while(lst>0):
    temp=lst%10
    su=su+temp
    lst=lst//10
print(su)
