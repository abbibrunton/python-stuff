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


def remove_person(n):
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	new_file = open("C:/Users/Admin/Documents/Python/new_file.txt", "w")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  ))
	i = 0
	while i <= count:
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
	while j <= count:
		file.write(new_file.readline())
		j += 1
	return (list_records())

print(remove_person(2))