def is_prime(n):
	"""
	Check if n is a prime
	"""
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True

def largest_prime(x):
	"""
	Finds the largest prime factor of X
	"""
	prime_list = []
	divide_list = []
	for i in range(2, x+1):
		if x%i == 0:
			divide_list.append(i)
	for num in divide_list:
		if is_prime(num):
			prime_list.append(num)
	print max(prime_list)