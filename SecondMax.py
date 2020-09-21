a = int(input())
max1 = a
a = int(input())
if a != 0:
	max2 = 0
	isDiff = False
	if a > max1:
		max2 = max1
		max1 = a
		isDiff = True
	else:
		max2 = a
		if a != max1:
			isDiff = True
	a = int(input())
	while a != 0:
		if a > max1:
			max2 = max1
			max1 = a
			isDiff = True
		elif a > max2:
			max2 = a
			isDiff = True
		a = int(input())
	if isDiff:
		print(max2)
	else:
		print("NO")
else:
	print("NO")
