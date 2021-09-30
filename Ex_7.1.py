file = open("mbox-short.txt")
for lines in file:
	a = lines.rstrip()
	if a == "":
		continue
	words = a.split()
	if words[0] != "From":
		continue
	print(words[2])