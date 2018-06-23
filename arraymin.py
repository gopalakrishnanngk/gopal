n=int(input())
s=input()
list=s.split()
m=int(list[0])
for i in range(1,n):
	if(m>int(list[i])):
		m=int(list[i])	
print(m)
