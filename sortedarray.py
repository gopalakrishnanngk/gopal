n=int(input())
s=input()
a=s.split()
m=[]
for i in range(0,n):
	b=int(a[i])
	m.append(b)
p=sorted(m)
q=[]
for i in range(0,n):
	q.append(str(p[i]))
print(" ".join(q))
