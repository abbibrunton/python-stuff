word = input("please enter a word: ")
word_lower = word.lower()
vowels = "aeiou"
count = 0
for char in word.lower():
	if char in vowels:
		count += 1
	else:
		continue
if count == 1:
	print("there is 1 vowel in", word)
else:
	print("there are", count, "vowels in", word)