s=input()
a=s.split()
n=int(a[0])
m=int(a[1])
num=[str(x) for x in range(n+1,m) if(x%2!=0)]
print(" ".join(num))
	
