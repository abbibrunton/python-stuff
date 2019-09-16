print("welcome to the calculator application!")
state = True

while state == True:
	number1 = int(input("enter the first number: "))
	number2 = int(input("enter the second number: "))

	print("option 1 - addition")
	print("option 2 - subtraction")
	print("option 3 - division")
	print("option 4 - multiplication")

	selection = int(input("please choose an option out of 1, 2, 3 or 4: "))

	if selection==1:
		answer = number1 + number2
		print(number1, "+", number2, "=", answer)
	elif selection==2:
		answer = number1 - number2
		print(number1, "-", number2, "=", answer)
	elif selection==3:
		if number2 != 0:
			answer = number1 / number2
			print(number1, "/", number2, "=", answer)
		else:
			print("sorry, you cannot divide by 0")
	elif selection==4:
		answer = number1 * number2
		print(number1, "*", number2, "=", answer)
	else:
		print("this is not a recognised selection")

	new_state = input("would you like to do another calculation? please enter y or n: ")
	if new_state.lower() == "n" or new_state.lower() == "no":
		state = False
	elif new_state.lower() == "y" or new_state.lower() == "yes":
		continue
	else:
		print("that is not a recognised response")
			
