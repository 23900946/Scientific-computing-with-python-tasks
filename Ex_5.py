num = 0
total = 0
while True:
	number = input("Enter a number: ")
	if number == "done":
		break
	try:
		a = float(number)
	except:
		print("Not valid")
		continue
	num = num + 1
	total = total + a
print("Done")
print(total, num, total/num)
	