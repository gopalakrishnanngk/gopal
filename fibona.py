n=int(input())
a=['1','1']
for i in range(2,n):
	b=str(int(a[i-2])+int(a[i-1]))
	a.append(b)
print(" ".join(a))	
