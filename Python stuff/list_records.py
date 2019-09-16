def list_records(b):
	file = open("C:/Users/Admin/Documents/Python/users.txt", "r")
	count = len(open("C:/Users/Admin/Documents/Python/users.txt", "r").readlines(  )) #this counts the number of lines in the file
	i = 1
	all_lines = []
	line = []
	while i <= count
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

print(list_records())