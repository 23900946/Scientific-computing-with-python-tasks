file = open("mbox-short.txt")
for lines in file:
	a = lines.rstrip()
	print(a.upper())