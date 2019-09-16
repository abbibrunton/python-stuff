number = 1

for number in range(1, 101):
	square = number**2
	if square < 2000:
		print(number, "squared is: ", square)
		number += 1
	else:
		break