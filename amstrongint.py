y=150
z=160
for num in range(y,z):
	order = len(str(num))
	sum = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		sum += digit ** order
		temp //= 10 
	if num == sum:
	    print(num)
