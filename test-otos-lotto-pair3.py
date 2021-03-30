
# PAIR3
#
# This program is part of a series of programs for the Hungarian public lucky game (ötöslottó)
# This game is a national-wide lottery:
# 	-- There are 5 draws from 90 numbers (01-90)
# 	-- There is one draw in each week
# 	-- Game began in 1957 back in the communist era
#	-- We have the data from all the draws.
#
#
# Written by Zoltan Dul (2021)
#
from typing import Dict

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import csv
import sys

# Import all the draws for into a dataframe using pandas
# Data is located in data/otos.csv
otos = pd.read_csv("data/lotto/source/otos.csv", sep=";", usecols=["Year", "Week", "Nr1", "Nr2", "Nr3", "Nr4", "Nr5"])

#
# Calculate all the options for 2 pairs
#

pair3_alloptions = {}
counter = 0
for i in range(1, 89):
	start2 = i + 1
	for j in range(start2, 90):
		start3 = j + 1
		for k in range(start3, 91):
			option = str(i).zfill(2) + "_" + str(j).zfill(2) + "_" + str(k).zfill(2)
			pair3_alloptions[option] = 0
			counter += 1

print(f"Parser have found {counter} 3-pair options between 1-90 numbers.")

#
# Retrieve and calculate all the occurred options
#

pair3_array = {}

for i in range(1, 4):
	i2 = i + 1
	for j in range(i2, 5):
		i3 = j + 1
		for k in range(i3, 6):
			this_nr1 = "Nr" + str(i)
			this_nr2 = "Nr" + str(j)
			this_nr3 = "Nr" + str(k)

			this_pair = otos.groupby([this_nr1, this_nr2, this_nr3]).size()

			for iterit in this_pair.iteritems():

				pair3_key = str(iterit[0][0]).zfill(2) + "_" + str(iterit[0][1]).zfill(2) + "_" + str(iterit[0][2]).zfill(2)
				pair3_num = int(iterit[1])

				if pair3_key in pair3_array:
					pair3_array[pair3_key] += pair3_num
				else:
					pair3_array[pair3_key] = pair3_num

				pair3_alloptions[pair3_key] += pair3_num

sorted_pair3 = sorted(pair3_array.items())
# print(sorted_pair2)
# print(pair2_alloptions)

export_filename = "data/lotto/export/otos_pair3_count.tsv"

with open(export_filename, mode='w') as export_file:
	writer = csv.writer(export_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for this_line in pair3_alloptions.items():
		writer.writerow(this_line)

	print(f"Parser have found {len(pair3_array)} empiric options.")
	print(f"Wrote in {export_filename} file.")

