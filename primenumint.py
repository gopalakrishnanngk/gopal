s=input()
a=s.split()
n=int(a[0])
m=int(a[1])
b=[]
for num in range(n,m):
	p=0
	if num>1:
		for i in range(2,num):
			if(num%i==0):
				p=1
		if(p==0):
			b.append(str(num))
print(" ".join(b))
				
