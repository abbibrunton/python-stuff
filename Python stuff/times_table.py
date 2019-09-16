# number = 1
# row1 = []
# for number in range(1,11):
# 	row1.append(str(number))
# 	number += 1
# row1_new = "   ".join(row1)
# print(row1_new)

for i in range(1,11):
	row = []
	for j in range(1,11):
		row.append(str(i*j))	
	row_new = "	".join(row)
	print(row_new)
