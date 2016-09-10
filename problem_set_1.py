def multiples_3_5_sum(x):
	"""
	Finds the sum of all multiples of 3 and 5 up to the number "x" (but not including x)
	"""
	sum_total = 0
	for i in range(1,x):
		if i%3 == 0:
			sum_total += i
		elif i%5 == 0:
			sum_total += i
	print sum_total

multiples_3_5_sum(1000)