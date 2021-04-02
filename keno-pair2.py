
# This program is part of a series of programs for the Hungarian public lucky game (Keno) to test Python
# This game is a national-wide lottery:
# 	-- There are 20 draws from 80 numbers (01-80)
# 	-- There is one draw in each day
# 	-- Game began in 1996
#	-- We have the data from all the draws.
#
#
# Written by Zoltan Dul (2021)
#

from typing import Dict
import pandas as pd
import csv

# Import all the draws for into a dataframe using pandas
# Data is located in data/lotto/source/keno.csv
keno = pd.read_csv("data/lotto/export/keno_create8.csv", sep=";", index_col=None, usecols=["Nr1", "Nr2", "Nr3", "Nr4", "Nr5", "Nr6", "Nr7", "Nr8", "Nr9", "Nr10",
																						   "Nr11", "Nr12", "Nr13", "Nr14", "Nr15", "Nr16", "Nr17", "Nr18", "Nr19", "Nr20"])
#
# Calculate all the options for 2 pairs
# Format of a pair like: "01_02"
#

# Pair-2 container dict
pair2_alloptions = {}
# Pair-2 counter
counter = 0

# First position: Cycle numbers from 1 to 79
for i in range(1, 80):
	start = i + 1
	# Second position: Cycle numbers from 2 to 80
	for j in range(start, 81):
		option = str(i).zfill(2) + "_" + str(j).zfill(2)
		pair2_alloptions[option] = 0
		counter += 1

# Write the results to the console
print(f"Parser have found {counter} 2 pair options between 1-80 numbers (Keno).")

#
# Retrieve and calculate all the occurred options
# Iterating the keno dataframe
#

# Array container for the pairs
pair2_array = {}

# 1-19 cycles for the Number 1 option.
for i in range(1, 20):

	# Number 1 options 1-19
	this_nr1 = "Nr" + str(i)
	# Number 2 options start (2-20)
	i2 = i + 1

	# 2-20 cycles for the Number 2 option.
	for j in range(i2, 21):

		# Number 2 options 2-20
		this_nr2 = "Nr" + str(j)

		# Pairing Nr1 and Nr2
		# Retreiving the common number by groupby function of pandas lib
		this_pair = keno.groupby([this_nr1, this_nr2]).size()

		for iterit in this_pair.iteritems():

			# Pair Nr1 and Nr2 as Nr1_Nr2 like.: 01_02 OR 19_20
			pair2_key = str(iterit[0][0]).zfill(2) + "_" + str(iterit[0][1]).zfill(2)
			pair2_num = int(iterit[1])

			if pair2_key in pair2_array:
				pair2_array[pair2_key] += pair2_num
			else:
				pair2_array[pair2_key] = pair2_num

			pair2_alloptions[pair2_key] += pair2_num

sorted_pair2 = sorted(pair2_array.items())
# print(sorted_pair2)
# print(pair2_alloptions)

# Export filename
export_filename = "data/lotto/export/keno_pair2_count_p1.tsv"

# Writing out the file
with open(export_filename, mode='w') as export_file:
	writer = csv.writer(export_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for this_line in pair2_alloptions.items():

		# this_line = str(cells[0]) + "\t" + str(cells[1])
		writer.writerow(this_line)

	print(f"Parser have found {len(pair2_array)} empiric options.")
	print(f"Wrote in {export_filename} file.")

