inp=int(input())
inp2=input()
list=inp2.split(" ")
lis=[]
for i in range(0,inp):
	lis.append(int(list[i]))

s=sorted(lis)
p=[]
for i in range(0,inp):
	p.append(str(s[i]))
print(" ".join(p))
