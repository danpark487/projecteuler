import math
def prime_factors(n):
	"""
	create list of prime factors for int(n)
	"""
    i = 2
    factors = []
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
	return factors

def least_common_multiple(num):
	"""
	find LCM of every number from range of 1 to num
	"""
	factors_list = []
	for i in range(2,num+1):
		factors_list.append(prime_factors(i))
	print factors_list
	counter = 2
	count_list = []
	final_solution = 1
	while counter < num:
		for x in factors_list:
			count_list.append(x.count(counter))
		if max(count_list) > 0:
			final_solution *= counter**max(count_list)
		counter += 1
		del count_list[:]
	print final_solution

least_common_multiple(20)