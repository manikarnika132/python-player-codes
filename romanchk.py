x=raw_input('enter a roman numeral\n')
num=0
for str in x:
	if(str=='I'): num+=1
	if(str=='V'): num+=5
	if(str=='X'): num+=10
	if(str=='L'): num+=50
	if(str=='C'): num+=100
	if(str=='D'): num+=500
	if(str=='M'): num+=1000
print num
