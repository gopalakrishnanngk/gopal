a=int(input())

b=int(input())

evens=[str(x) for x in range(a+1,b-1) if x%2==0]

odds=[str(x) for x in range(a+1,b) if x%2==1]

print("\t"+"\t".join(odds))
