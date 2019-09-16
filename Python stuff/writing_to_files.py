file = open("filename.txt","w")
for n in range (1,11):
	newline = "this is line " + str(n) + "\n"
	file.write(newline)
file.close()

file = open("filename.txt","r")

print("first line: " +file.readline())
print("second line: " + file.readline())
print("rest of file: " + file.read())
print("blank line: " +file.readline())
