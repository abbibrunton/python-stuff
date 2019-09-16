#check for word in list of words file
def check(word_1):
	found = False
	file = open("list_of_words.txt", "r")
	file_list = []
	for i in range(69903):
		file_list.append((file.readline()).strip("\n"))
	
	for word in file_list:
		if word_1 == word:
			found = True
			break
	file.close()
	return found

# word = input("enter your word: ")
word = "before"

len_word = len(word)
possible_words = []
letters_string = ""
# creates an empty string to fill. this will be the parameter for the check function
i = 0
if i < len_word:
	j = 0
	k = i+j
	while k<=(len_word-1):
		letters_string += word[i+j]
		if check(letters_string):
			print(letters_string)
			possible_words.append(letters_string)
			i+=1
		else:
			continue
		j+=1


