print("menu")
print("1 - add")
print("2 - amend")
print("3 - delete")
print("4 - display")

menu_option = int(input("enter option: "))

if menu_option == 1:
	print("option 1 - add selected")
elif menu_option == 2:
	print("option 2 - amend selected")
elif menu_option == 3:	
	print("option 3 - delete selected")
elif menu_option == 4:
	print("option 4 - display selected")
else:
	print("this is not a recognised option")
