t=int(input())
count=0
for I in range(t):
    a,b,c=map(int,input().split())
    if a+b+c>1:
        count+=1
print(count)   
    