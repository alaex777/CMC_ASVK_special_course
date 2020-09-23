def isPairCubes(num):
	for i in range(1,int(num ** (1/3))):
		for j in range(1,int(num ** (1/3))):
			if i ** 3 + j ** 3 == num:
				return "YES"
	return "NO"
n = int(input())
print(isPairCubes(n))
