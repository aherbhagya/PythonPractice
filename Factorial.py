def factorial(no):
	fact=1
	while no >1:
		fact=fact*no
		no=no-1
	return fact
no=6
print factorial(no)