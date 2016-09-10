def fibo(n):
	if n < 2:
		return 1
	else:
		return fibo(n-2) + fibo(n-1)
		
n = 1
result = 0

while fibo(n-2) + fibo(n-1) < 4000000:
	if fibo(n)%2 == 0:
		result += fibo(n)
		n += 1
	else:
		n += 1
print result