n=int(input())
a=list(map(int,input().split()))
ser=0
dim=0
order=3
while len(a)!=0:
    if order%2!=0:
        if a[0]>a[-1]:
            ser+=a[0]
            a.pop(0)
            order+=1          
        else:
            ser+=a[-1]
            a.pop()
            order+=1
    else:
        if a[0]>a[-1]:
            dim+=a[0]
            a.pop(0)
            order+=1          
        else:
            dim+=a[-1]
            a.pop()
            order+=1
print(ser,dim)