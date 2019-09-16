	
state = True
while state == True:
	choice = input("please select an option.\n 1: view the records in the file\n 2: add a new person to the file\n 3: remove a person from the file\n 4: view information about a specific person\n 5: create a backup of the file\n your selection: ")

	if choice == 1:
		print(list_records)
	elif choice == 2:
		first_name = input("enter first name: ")
		last_name = input("enter last name: ")
		add1 = input("enter first line of address: ")
		add2 = input("enter town/city: ")
		postcode = input("enter postcode: ")
		number = input("enter phone number: ")
		print(add_person(first_name, last_name, add1, add2, postcode, number))
	elif choice == 3:
		id_to_remove = input("enter the id of the person you want to remove: ")
		print(remove_person(int(id_to_remove)))
	elif choice == 4:
		field = input("choose a field to search by:\n 1: id number\n 2: first name\n 3: last name\n 4: first line of address\n 5: town/city\n 6: postcode\n 7: phone number\n your selection: ")
		input_1 = input("enter the information in this field to search for: ")
		print(tell_me(input_1, int(field)))
	elif choice == 5:
		print(copy_doc())
	else:
		print("that is not a recognised response.")

	new_state = input("would you like to do another function? please enter y or n: ")
	if new_state.lower() == "n" or new_state.lower() == "no":
		state = False
	elif new_state.lower() == "y" or new_state.lower() == "yes":
		continue
	else:
		print("that is not a recognised response")