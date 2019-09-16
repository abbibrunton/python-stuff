print("menu")
print("1 - level 1")
print("2 - level 2")
print("3 - level 3")
print("3 - level 4")

examlevel = int(input("enter exam level: "))

if examlevel==1 or examlevel==2:
	mark = int(input("enter level 1 or 2 mark: "))
	if mark >= 75:
		print("pass")
	else:
		print("fail")
elif examlevel==3 or examlevel==4:
	mark = int(input("enter level 3 or 4 mark: "))
	if examlevel==3 and mark >= 65:
		print("pass")
	elif examlevel==4 and mark >= 50:
		print("pass")
	else:
		print("fail")
else:
	print("invalid level")
	