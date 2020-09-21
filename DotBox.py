a = input()
coords = a.split(",")
x = float(coords[0])
y = float(coords[1])
z = float(coords[2])
minx = maxx = x
miny = maxy = y
minz = maxz = z
a = input()
while a != "":
	coords = a.split(",")
	x = float(coords[0])
	y = float(coords[1])
	z = float(coords[2])
	if x > maxx:
		maxx = x
	if x < minx:
		minx = x
	if y > maxy:
		maxy = y
	if y < miny:
		miny = y
	if z > maxz:
		maxz = z
	if z < minz:
		minz = z
	a = input()
print((maxx - minx) * (maxy - miny) * (maxz - minz))

