n=int(input())
arr=[int(x) for x in input().split()]
def merge(l):
    if(len(l)>1):
        mid=len(l)//2
        L=l[:mid]
        R=l[mid:]
        merge(L)
        merge(R)
        i=k=j=0
        while i<len(L) and j<len(R):
            if(L[i]<R[j]):
                l[k]=L[i]
                i+=1
            else:
                l[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            l[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            l[k]=R[j]
            j+=1
            k+=1
        return l
h=merge(arr)
for i in h:
    print(i,end=" ")
