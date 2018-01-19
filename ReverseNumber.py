def reverse(no):
	rev=0
	while no :
		r=no%10
		rev=rev*10+r
		no=no/10
	return rev
no=1234
print reverse(no)
