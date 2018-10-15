n=input()
a=n.split()
l=int(a[1])
b=str(a[0])
m=len(b)
z=[]
if(l<m):
    x=int(m)-int(l)
    for i in range(l-1,-1,-1):
        y=b[i+x]
        z.append(y)
        p=z[::-1]
    print("".join(p))
elif(l==m):
	for i in range(l-1,-1,-1):
		z.append(b[i])
	print("".join(z[::-1]))
