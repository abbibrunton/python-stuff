file = open("filename.txt", "r")
# file.seek(0)
lines_needed = ""
file.seek(0)
file.readline()
lines_needed += file.read()

file = open("filename.txt", "w")
file.write("this is a new line \n")
file.write(lines_needed)

file.close()