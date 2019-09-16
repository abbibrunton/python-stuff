#create a function which will list all the records that are specified in the text file

def list_records():
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  )) #this counts the number of lines in the file
	i = 1
	all_lines = []
	line = []
	while i <= count:
		if i % 7 != 0: #each block of data is 7 lines long
			line.append(file.readline().strip("\n"))
		else:
			line.append(file.readline().strip("\n"))
			all_lines.append(line)
			print(line)
			line = []
		i += 1
	return(all_lines)
	file.close()

#create a function that will add a person to the text file following the existing format
#to find the id number i want to use, i want to find the length of the file. i can use count from earlier. from there, i want to take the (count - 7)th entry and add 1 to it. this will create a unique id.
def add_person(first, last, add1, add2, postcode, number):
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  ))
	file.seek(0)
	latest_id = int(open('C:/Users/Admin/Documents/Python/users.txt').readlines()[count-7])
	file.close()
	file = open("C:/Users/Admin/Documents/Python/users.txt", "a")
	id_number = latest_id + 1
	#now i am adding the inputted data as separate lines
	file.write("\n")
	file.write(str(id_number))
	file.write("\n")
	file.write(first)
	file.write("\n")
	file.write(last)
	file.write("\n")
	file.write(add1)
	file.write("\n")
	file.write(add2)
	file.write("\n")
	file.write(postcode)
	file.write("\n")
	file.write(number)
	latest_id += 1
	file.close()
	return("person added successfully.")
		
# create a function to remove a particular person from the text file
def remove_person(n):
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	new_file = open("C:/Users/Admin/Documents/Python/new_file.txt", "w")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  ))
	i = 0
	while i <= count-1:
		if i < (7*n-7):
			new_file.write(file.readline())
			i += 1
		elif i > 7*n - 1:
			new_file.write(file.readline())
			i += 1
		else:
			file.readline()
			i += 1		
	file.close()
	new_file.close()
	file = open("C:/Users/Admin/Documents/Python/users.txt", "w")
	new_file = open("C:/Users/Admin/Documents/Python/new_file.txt", "r")
	j = 0
	while j <= count-1:
		file.write(new_file.readline())
		j += 1
	#for some reason when you add a user, remove a user, and add another one it creates a blank line which messes up the formatting for the rest of the code since it relies on everything being on the correct line. i can't work out how to sort this out :(
	return ("removed successfully.")

#create a function that can list information about a person that exists in the text file
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

#create a function that can make a copy of the text file to be used as a back-up
import shutil
def copy_doc():
	path = "C:/Users/Admin/Documents/Python"
	source = "C:/Users/Admin/Documents/Python/users.txt"
	destination = "C:/Users/Admin/Documents/Python/users_copy.txt"
	dest = shutil.copyfile(source, destination)
	return("copy completed. destination path: ", dest)

#create a function to update a person that already exists in the text file
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

#this allows the user to choose what they would like to do
state = True
while state == True:
	choice = input("please select an option.\n 1: view the records in the file\n 2: add a new person to the file\n 3: remove a person from the file\n 4: view information about a specific person\n 5: create a backup of the file\n 6: update a person in the file\n your selection: ")

	if choice == "1":
		print(list_records())
	elif choice == "2":
		first_name = input("enter first name: ")
		last_name = input("enter last name: ")
		add1 = input("enter first line of address: ")
		add2 = input("enter town/city: ")
		postcode = input("enter postcode: ")
		number = input("enter phone number: ")
		print(add_person(first_name, last_name, add1, add2, postcode, number))
	elif choice == "3":
		id_to_remove = input("enter the id of the person you want to remove: ")
		print(remove_person(int(id_to_remove)))
	elif choice == "4":
		field = input("choose a field to search by:\n 1: id number\n 2: first name\n 3: last name\n 4: first line of address\n 5: town/city\n 6: postcode\n 7: phone number\n your selection: ")
		input_1 = input("enter the information in this field to search for: ")
		print(tell_me(input_1, int(field)))
	elif choice == "5":
		print(copy_doc())
	elif choice == "6":
		id_number = input("enter the id number of the person you want to update: ")
		field = input("enter the field you would like to update:\n 1: id number\n 2: first name\n 3: last name\n 4: first line of address\n 5: town/city\n 6: postcode\n 7: phone number\n your selection: ")
		update = input("what would you like to replace this with?: ")
		print(update_person(id_number, field, update))
	else:
		print("that is not a recognised response.")

	new_state = input("would you like to do another function? please enter y or n: ")
	if new_state.lower() == "n" or new_state.lower() == "no":
		state = False
	elif new_state.lower() == "y" or new_state.lower() == "yes":
		continue
	else:
		print("that is not a recognised response")
