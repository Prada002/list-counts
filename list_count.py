a=[2,2,3,5,4,5,8,4,7,5,9,7,2,1,4,6,8,9,3]
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
print(b)