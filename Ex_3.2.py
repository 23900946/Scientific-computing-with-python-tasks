hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
	a = float(hours)
	b = float(rate)
except:
	print("Please enter a number")
	quit()
	
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