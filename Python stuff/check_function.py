file_list = []
file = open("list_of_words.txt", "r")
for i in range(69903):
	file_list.append((file.readline()).strip("\n"))


print(file_list[:10])
