s=input()
a=s.split()
p=int(a[0])
q=int(a[1])
b=[]
for num in range(p,q):
	m=str(num)
	n=len(m)
	sum=0
	for i in range(n):
		c=m[i]
		e=int(c)
		d=e**n
		sum=sum+d
	if(sum==num):
		b.append(m)
print(" ".join(b))
				
	
