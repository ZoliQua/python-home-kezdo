
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
from typing import Dict

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import csv
import sys

# Import all the draws for into a dataframe using pandas
# Data is located in data/lotto/source/keno.csv
keno = pd.read_csv("data/lotto/source/keno.csv", sep=";", usecols=["Year", "Week", "Nr1", "Nr2", "Nr3", "Nr4", "Nr5", "Nr6", "Nr7", "Nr8", "Nr9", "Nr10",
																   "Nr11", "Nr12", "Nr13", "Nr14", "Nr15", "Nr16", "Nr17", "Nr18", "Nr19", "Nr20"])

#
# Calculate all the options for 2 pairs
#

pair2_alloptions = {}
counter = 0
for i in range(1, 80):
	start = i + 1
	for j in range(start, 81):
		option = str(i).zfill(2) + "_" + str(j).zfill(2)
		pair2_alloptions[option] = 0
		counter += 1

print(f"Parser have found {counter} 2 pair options between 1-80 numbers (Keno).")

#
# Retrieve and calculate all the occurred options
#

pair2_array = {}

for i in range(1, 20):

	i2 = i + 1

	for j in range(i2, 21):
		this_nr1 = "Nr" + str(i)
		this_nr2 = "Nr" + str(j)

		this_pair = keno.groupby([this_nr1, this_nr2]).size()

		for iterit in this_pair.iteritems():

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

export_filename = "data/lotto/export/keno_pair2_count.tsv"

with open(export_filename, mode='w') as export_file:
	writer = csv.writer(export_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# for this_line in sorted_pair2:
	#
	# 	counter += 1
	# 	# this_line = str(cells[0]) + "\t" + str(cells[1])
	# 	writer.writerow(this_line)

	for this_line in pair2_alloptions.items():

		# this_line = str(cells[0]) + "\t" + str(cells[1])
		writer.writerow(this_line)

	print(f"Parser have found {len(pair2_array)} empiric options.")
	print(f"Wrote in {export_filename} file.")


#
# # Text for the x axis
# plt.xlabel("List of Numbers (1-90)")
# # Text for the y axis
# plt.ylabel("Number of occurrences")
# # Title of the plot
# plt.title("keno Lotto Szamok")
# # Plotting
# plt.plot(keno_lotto_szamok_count, "-", label="Counts", linewidth=2, color="orange")
# # Create the legend for the figure
# plt.legend()
# # Save the file
# # plt.savefig('images/jpgImageDir/line_plot_' + current_time_abbrev + '.jpg', dpi=300)
# # Show the file
# plt.show()
