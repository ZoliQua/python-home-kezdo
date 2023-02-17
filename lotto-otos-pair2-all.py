
#test file

for i in range(1, 90):
	start = i + 1
	for j in range(start, 91):
		toprint = str(i).zfill(2) + "_" + str(j).zfill(2)
		print(toprint)
