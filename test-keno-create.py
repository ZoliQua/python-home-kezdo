
# This program is part of a series of programs for the Hungarian public lucky game (Keno)
# This game is a national-wide lottery:
# 	-- There are 20 draws from 80 numbers (01-80)
# 	-- There is one draw in each day
# 	-- Game began in 1996
#	-- We have the data from all the draws.
#
#
# Written by Zoltan Dul (2021)
#

import csv
import random

#
# Creating a random Keno
#

# Adding spaceholder text for the beginning of the file
line_starter = ";99;9;2022.12.31."
lines = ["Year;Week;Day;Date;Nr1;Nr2;Nr3;Nr4;Nr5;Nr6;Nr7;Nr8;Nr9;Nr10;Nr11;Nr12;Nr13;Nr14;Nr15;Nr16;Nr17;Nr18;Nr19;Nr20"]

# Random cycles for create numbers

for i in range(0,8503):
	line_num = i + 1000
	nrs = []
	# Creating random 20 numbers
	while len(nrs) < 20:
		rnd = str(random.randrange(1, 81)).zfill(2)
		# Until we find 20 unique numbers between 1 - 80
		if rnd not in nrs:
			nrs.append(rnd)

	nrs.sort()
	this_line = str(line_num) + line_starter + ";" + ";".join(nrs)
	lines.append(this_line)


# Export & print results in file

# Random tag
rnd = str(random.randrange(1, 9))
# Filename
export_filename = "data/lotto/export/keno_create" + rnd + ".csv"

with open(export_filename, mode='w') as export_file:
	writer = csv.writer(export_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for line in lines:
		this_line = line.split(";")
		writer.writerow(this_line)

