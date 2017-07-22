# pattern 1
import sys
x=input('enter a number\n')
for i in range(0,x):
	k=x-i+1
	for m in range(k):
		sys.stdout.write(' ')
	for j in range(i+1,0,-1):
		sys.stdout.write('%d'%(j))
	print


#pattern 2
import sys
x=input('enter a number\n')
for i in range(-1,x):
	k=x-i+1
	for m in range(k):
		sys.stdout.write(' ')
	for j in range(2*i+1,0,-1):
		sys.stdout.write('*')
	print


#pattern 3
import sys
x=input('enter a number\n')
for i in range(-1,x):
	k=x-i+1
	for m in range(k):
		sys.stdout.write(' ')
	for j in range(2*i+1,0,-1):
		sys.stdout.write('*')
	print
for i in range(x-1,-1,-1):
	k=x-i+1
	for m in range(k):
		sys.stdout.write(' ')
	for j in range(2*i+1,0,-1):
		sys.stdout.write('*')
	print
