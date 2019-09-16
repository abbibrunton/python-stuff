id_number = input("enter the id number of the person you want to update: ")
field = input("enter the field you would like to update:\n 1: id number\n 2: first name\n 3: last name\n 4: first line of address\n 5: town/city\n 6: postcode\n 7: phone number\n your selection: ")
update = input("what would you like to replace this with?: ")

def update_person(id, field, input):
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	update_file = open("C:/Users/Admin/Documents/Python/update_file.txt", "w")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  ))

	start = int(id)*7 - 6 #finds the start of the information about this person
	field_location = start + int(field) + 1 #finds the line with the field that wants to be updated
	for i in range(count+1):
		if i+3 != field_location: #i dont know why it has to be i+3 but thats the only one that works so.....
			update_file.write(file.readline())
		else:
			update_file.write(input)
			update_file.write("\n")
			file.readline()
	file.close()
	update_file.close()
	file = open("C:/Users/Admin/Documents/Python/users.txt", "w")
	update_file = open("C:/Users/Admin/Documents/Python/update_file.txt", "r")
	j = 0
	while j <= count:
		file.write(update_file.readline())
		j += 1
	return("updated successfully.")

print(update_person(id_number, field, update))


