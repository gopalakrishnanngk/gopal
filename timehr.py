p=input()
s=int(p)
n=[]
if s>=60:
	a=s/60
	b=s%60
	a=int(a)
	n.append(a)
	n.append(b)
	print(" ".join(str(x) for x in n))
else:
	print("0 "+"".join(p))
