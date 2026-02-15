t=int(input())
count=1
lst=[]
for i in range(t):
    n=input()
    lst.append(n)
for j in range(len(lst)-1):
    if lst[j]==lst[j+1]:
        continue
    else:
        count+=1
print(count)