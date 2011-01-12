from math import sqrt

def fibo(n):
	return int(round((1/sqrt(5))*pow(((1+sqrt(5))/2), n)))

f = 0
x = 1
summa = 0
finished = False
while not finished:
	f = fibo(x)
	x += 1
	if f % 2 == 0: 
		if f <= 4000000:
			print f
			summa += f
		else:
			finished = True

print summa


