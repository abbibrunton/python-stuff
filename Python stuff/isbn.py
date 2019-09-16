isbn_number = input("enter the ISBN number: ")

isbn_stripped = str(isbn_number.replace("-",""))

sum1 = 0

i = 0
print(isbn_stripped)

while i < 12:
	if i % 2 == 0:
		sum1 += int(isbn_stripped[i])
	elif i % 2 == 1:
		sum1 += (3*int(isbn_stripped[i]))
	else:
		continue
	i += 1	
print(sum1)

remainder = float(sum1 % 10)
check_digit = 10 - remainder

print(check_digit)