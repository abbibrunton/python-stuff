file = open("teams.txt", "w")
file.write("man city \n")
file.write("man u \n")
file.write("the los angeles angels \n")
file.write("reading \n")
file.write("sharks \n")

file.close()

file = open("teams.txt", "r")
print("team 1:", file.readline())
print("team 2:", file.readline())

file.close()