p=input()
q=input()
a=p.split()
b=q.split()
n=int(a[0])
m=int(a[1])
j=int(b[0])
k=int(b[1])
z=[]
if n>=j:
	x=n-j
	y=m-k
	z.append(x)
	z.append(y)
	print(" ".join(str(i) for i in z))
else:
	x=j-n
	y=k-m
	z.append(x)
	z.append(y)
	print(" ".join(str(i) for i in z))
	
