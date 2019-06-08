B=input()
B=int(B)
YZ=[]
for j in range(0,B):  
    num1=input()
    YZ.append(num1)
x1=[]
for j in zip(*YZ):
    if j.count(j[0])==len(j): 
        x1.append(j[0])
    else:
        break
print(''.join(x1))
