# field = input("choose a field to search by:\n 1: id number\n 2: first name\n 3: last name\n 4: first line of address\n 5:town/city\n 6: postcode\n 7: phone number\n your selection: ")
def tell_me(user_input, field):
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  ))
	found = False
	found_list = []
	i = 0
	while found == False:
		while i < count:
			line = str(file.readline())
			if user_input in line:
				found = True
				found_list.append(i)
				i += 1
			else:
				i += 1 
	people = []
	person_data = []
	for item in found_list:
		person_data = []	
		start = int(item) - int(field) + 1 #i now refers to what line the item has been found in. the start subtracts the field number to find the line that the person's data begins at.
		file.seek(0)
		j = 0
		while j < start:
			file.readline()
			j += 1
		while start <= j <= start + 6:
			person_data.append(file.readline().strip("\n"))
			j += 1
		#print(person_data)
		people.append(person_data)
	return(people)

print(tell_me("Geoff", 2))