s=input()
a=s.split()
m=int(a[0])
n=int(a[1])
x=input()
x=x.split()
sum=0
for i in range(0,n):
	sum=sum+int(x[i])
print(sum)	
