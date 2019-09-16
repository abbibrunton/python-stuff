def near(word1, word2):
	i = 0
	status = False
	while i < len(word1):
		new_word = word1[:i] + word1[i+1:]
		if new_word == word2:
			status = True
			return(status)
		else:
			i+=1
	return(status)

		
print(near("reset","rest"))


# near("test", "T")
# word = "test"
# for letter in word:
# 	print(letter)
# l = list(word)

# print(l.remove("e"))
# print(l)