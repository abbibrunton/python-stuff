import shutil
def copy_doc():
	path = "C:/Users/Admin/Documents/Python"
	source = "C:/Users/Admin/Documents/Python/users.txt"
	destination = "C:/Users/Admin/Documents/Python/users_copy.txt"
	dest = shutil.copyfile(source, destination)
	return("copy completed. destination path: " +dest)

print(copy_doc())