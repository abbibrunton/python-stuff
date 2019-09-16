number1 = float(input("please enter first number: "))
number2 = float(input("please enter second number: "))
if number2 != 0:
	answer = number1 % number2
	print(answer)
else:
	print("sorry, you cannot divide by 0.")