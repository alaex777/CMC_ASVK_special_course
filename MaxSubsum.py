a = int(input())
maxSum = a
tmpSum = 0
while a != 0:
	tmpSum += a
	if tmpSum > maxSum:
		maxSum = tmpSum
	if tmpSum <= 0:
		tmpSum = 0
	a = int(input())
print(maxSum)