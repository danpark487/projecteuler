def sum_square(n):
	"""
	return sum of square of all positive integers up to and including n
	"""
	total = 0
	for i in range(1,n+1):
		total += i ** 2
	return total
	
def square_sum(n):
	"""
	return the square of sum of all positive integers up to and including n
	"""
	total = 0
	for i in range(1,n+1):
		total += i
	total = total ** 2
	return total

print square_sum(100) - sum_square(100)