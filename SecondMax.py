a = int(input())
max1 = a
a = int(input())
max2 = min(a, max1)
while a != 0:
	if a > max1:
		max2 = max1
		max1 = a
	elif a > max2:
		max2 = a
	a = int(input())
if max2 == max1:
	print("NO")
else:
	print(max2)