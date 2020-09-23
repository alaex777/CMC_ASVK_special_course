def isPrime(num):
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True

n = int(input())
while isPrime(n) == False:
	n -= 1
print(n)