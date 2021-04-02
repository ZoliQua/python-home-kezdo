import random

while True:

	input_txt = input('Nyomj egy számot (1-10), hogy hány 1-20 közötti random számot írjak vagy STOP-ot leállításhoz:\n')

	if input_txt.upper() == "STOP":
		print("A program STOP utasításra leáll.")
		break

	try:
		input_int = int(input_txt)
	except:
		print("Ez nem szám. A program kilép.")
		break

	if input_int > 0 and input_int < 10:

		ints_to_print = []
		for i in range(0, input_int):
			ints_to_print.append(str(random.randint(1,20)))

		print(", ".join([str(elem) for elem in ints_to_print]))

	else:
		print("A szám nem 1 és 10 közötti.")