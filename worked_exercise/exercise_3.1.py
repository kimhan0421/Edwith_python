sh = float(input("Enter Hours: "))
sr = float(input("Enter Rate: "))
if sh > 40 :
	reg = sr * sh #보통급여
	otp = (sh - 40.0) * (sr * 0.5)#초과급여
	#print(reg, otp)
	xp = reg + otp
else:
	#print("regular")
	xp = sh * sr
print("Pay:", xp)
