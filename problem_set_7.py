def isPrime(x):
	counter = 2
	while counter < x:
		if x%counter != 0:
			counter += 1
		else:
			return False
	return True


def prime_num(n):
	counter = 1
	num = 3
	while counter < int(n):
		if isPrime(num):
			counter += 1
		num += 2
	print num-2