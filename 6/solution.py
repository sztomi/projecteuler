def square_sum(n):
	return ((n*(n+1))/2)**2

def sum_of_squares(n):
	return (n*(n+1)*(2*n+1))/6

N = 100

print square_sum(N) - sum_of_squares(N)



