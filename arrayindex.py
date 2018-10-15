n=int(input())
s=input()
a=s.split()
m=[]
for i in range(0,n):
	b=str(a[i])+(' '+str(i))
	m.append(b)
print("\n".join(m))
