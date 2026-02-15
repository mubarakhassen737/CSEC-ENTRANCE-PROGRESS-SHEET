t=input()
count=0
lst=[]
for i in t:
    if i not in lst:
        lst.append(i)
        count+=1
if count%2==0:
    print('CHAT WITH HER!')             
else:
    print('IGNORE HIM!')