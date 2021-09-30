hours = input("Enter hours: ")
rate = input("Enter rate: ")
a = float(hours)
b = float(rate)
if a > 40:
	print("Overtime")
	pay = a * b
	otp = (a - 40.0) * (b * 0.5)
	c = pay + otp
	print(c)
	
else:
	print("Regular time")
	pay = a * b
	print(pay)