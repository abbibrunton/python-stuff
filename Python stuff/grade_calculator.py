print("welcome to grade calculator")
maths = float(input("what did you get in maths?: "))
chemistry = float(input("what did you get in chemistry?: "))
physics = float(input("what did you get in physics?"))

percentage = ((maths + chemistry + physics)/3)
print("your percentage score is " +str(percentage) +"%")

if percentage >= 70:
	print("A")
elif percentage >= 60:
	print("B")
elif percentage >= 50:
	print("C")
elif percentage >= 40:
	print("D")
else:
	print("you failed")