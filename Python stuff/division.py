number1 = float(input("please enter first number: "))
number2 = float(input("please enter second number: "))
if number2 != 0:	
	answer = number1 / number2
	print(number1, " / ", number2, " = ", answer)
else:
	print("Sorry, you cannot divide by 0.")