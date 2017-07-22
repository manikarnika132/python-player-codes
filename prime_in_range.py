def prime(num):
	c=0
	for i in range(2,num-1):
		if(num%i==0):
			c=c+1
	return c
x=input('enter a number\n')
y=input('enter a number\n')
v=0
if (x>y):
	for i in range(y,x):
		h=prime(i)
		if(h==0):
			v=v+1
else:
	for i in range(x,y):
		h=prime(i)
		if(h==0):
			v=v+1
print('the number of prime numbers are: {0}'.format(v))
