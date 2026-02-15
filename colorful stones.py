n=input()
t=input()
count=1
noth=0
for i in range(len(t)):
    if noth<len(n) and t[i]==n[noth]:
        count+=1
        noth+=1
print(count)