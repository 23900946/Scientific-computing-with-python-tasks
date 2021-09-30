def computePay(hours, rate):
	if hours > 40:
		print("Overtime")
		pay = hours * rate
		otp = (hours - 40.0) * (rate * 0.5)
		pay = pay + otp
		
	else:
		print("Regular time")
		pay = hours * rate
	print(pay)	
	return pay
	
hours = input("Enter hours: ")
rate = input("Enter rate: ")
a = float(hours)
b = float(rate)
computePay(a, b)