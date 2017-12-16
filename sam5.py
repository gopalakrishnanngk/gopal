a=34
b=44
c=87
print("the gretest number is")
if a<b:
	if b<c:
		print c
	else:
		print b
elif b<c:
	if c<a:
		print a
	else:
		print c
elif c<a:
	if a<b:
		print b
	else:
		print a
		# your code goes here