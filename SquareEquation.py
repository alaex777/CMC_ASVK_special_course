nums = [int(i) for i in input().split(",")]
a = nums[0]
b = nums[1]
c = nums[2]
if a == 0:
	if b == 0:
		print(-1)
	else:
		print(-c / b)
else:
	d = b ** 2 - 4 * a * c
	if d < 0:
		print(0)
	elif d == 0:
		print(-b / (2 * a))
	else:
		if a > 0:
			print((-b - d ** 0.5) / (2 * a),(-b + d ** 0.5) / (2 * a))
		else:
			print((-b + d ** 0.5) / (2 * a),(-b - d ** 0.5) / (2 * a))