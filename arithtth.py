def arithsum(n,a,d):
	sum=(n/2)*(2*a+(n-1)*d)
	return sum
n=int(input())
a=int(input())
d=int(input())
print(n, a, d)
print(int(arithsum(n,a,d)))
