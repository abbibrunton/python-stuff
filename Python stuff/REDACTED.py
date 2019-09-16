import random
import getpass

def word_check(word_1):
	found = False
	file = open("C:/Users/Admin/Documents/Python/list_of_words.txt", "r")
	file_list = []
	for i in range(69903):
		file_list.append((file.readline()).strip("\n"))
	
	for word in file_list:
		if word_1 == word:
			found = True
			break
	file.close()
	return found

points = {"a":1, "b":3, "c":3, "d":4, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8, "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1, "u":1, "v":4, "w":4, "x":8, "y":4, "z":10}
alphabet = "aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz"

player_1_letters = []
player_2_letters = []

for i in range(0,7):
	letter_number_1 = random.randint(0,97)
	letter = alphabet[letter_number_1]
	player_1_letters.append(letter)
	letter_number_2 = random.randint(0,97)
	letter = alphabet[letter_number_2]
	player_2_letters.append(letter)


print("welcome to REDACTED")

print("player 1, here are your letters: ", player_1_letters)
print("player 2, here are your letters: ", player_2_letters)

player_1_word = getpass.getpass("player 1, please enter your word: ")
player_2_word = getpass.getpass("player 2, please enter your word: ")


state_1 = True
for letter in player_1_word:
	if letter in player_1_letters:
		player_1_letters.remove(letter)
	else:
		state_1 = False
		break

state_2 = True
for letter in player_2_word:
	if letter in player_2_letters:
		player_2_letters.remove(letter)
	else:
		state_2 = False
		break

if not word_check(player_1_word):
	state_1 = False
else:
	blank = 0
if not word_check(player_2_word):
	state_2 = False
else:
	blank = 0


def score(word):
	player_score = 0
	for letter in word:
		player_score += int(points[letter])
	return(player_score)

if state_1 == True:
	print("player 1, your score is: ", score(player_1_word))
else:
	print("player 1, your word is not valid.")

if state_2 == True:
	print("player 2, your score is:", score(player_2_word))
else:
	print("player 2, your word is not valid.")

print("thank you for playing REDACTED")


#C:\Users\Admin\Documents\Python\list_of_words.txt