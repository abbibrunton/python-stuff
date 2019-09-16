units = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
tens = {2: " twenty",3: " thirty",4: " forty",5: " fifty",6: " sixty",7: " seventy",8: " eighty",9: " ninety"}
scales = {0 : "and", 1 : " hundred", 2 : " thousand", 3 : " million", 4 : " billion", 5 : " trillion", 6 : " ", 7 : "-"}

def rev(num):
	num = str(num)[::-1]
	l = []
	blocksOf3 = []
	numList = list(num)
	for i in range(1, len(num) +1):
		if (i % 3) == 0:
			l.append(numList[i-1])
			blocksOf3.append(l[::-1])
			l = []
		else:
			l.append(numList[i-1])
	if not l:
		blank = 0
	else:
		blocksOf3.append(l)
	blocksOf3_len = len(blocksOf3)
	blocksOf3.reverse()

	for a in blocksOf3:
		theWord = ""
		len_b = len(a)
		for b in a:
			if len_b == 3:
				if b != 0:
					theWord += units[int(b)]
					theWord += scales[6]
					theWord += scales[1] + scales[6] + scales[0] + scales[6]
			elif len_b ==2:
				theWord += tens[int(b)] + scales[7]
			elif len_b ==1:
				theWord += units[int(b)] + scales[6]
			len_b -= 1
		if blocksOf3_len >= 2:
			theWord += scales[int(blocksOf3_len)]
		blocksOf3_len -= 1
		print(theWord)
rev(578145849674181)