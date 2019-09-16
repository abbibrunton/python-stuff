strngth = input("Weak, Strong or Medium: ")
strngth = strngth.lower()

words = {5: "puppy", 6: "robots", 7: "balance", 8: "withdraw"}
letters = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l", 13:"m",14:"n",15:"o",16:"p",17:"q",18:"r", 19:"s",20:"t", 21:"u", 22:"v", 23:"w",24:"x",25:"y", 26:"z"}


import random

output = ""

if strngth == "weak":
	output += words[random.randint(5,8)]

elif strngth == "medium":
	b = int(input("How long? choose between 5-15: "))
	for n in range(b):
		if random.randint(0,1) == 0:
			output += letters[random.randint(1,26)]
		else:
			output += letters[random.randint(1,26)].upper()
		

	
elif strngth == "strong":
	b = int(input("How long? choose between 10-20: "))
	for i in range(b-6):
		if random.randint(0,1)==0:
			output += letters[random.randint(1,26)]
		else:
			output += letters[random.randint(1,26)].upper()
	for i in range(6):
		output += str(random.randint(0,9))
print("\n")
print(output)



