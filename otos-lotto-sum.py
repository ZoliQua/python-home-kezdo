
# This program counts the all occurrences of the numbers

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Import dataframe using pandas
otos = pd.read_csv("data/lotto/source/otos.csv", sep=";", usecols=["Year", "Week", "Nr1", "Nr2", "Nr3", "Nr4", "Nr5"])

otos_lotto_szamok = {}
otos_lotto_szamok_list = []
otos_lotto_szamok_count = []

for i in range(1, 6):
	name_of_this_nr = "Nr" + str(i)

	this_nr = otos.sort_values(by=[name_of_this_nr]).filter(items=[name_of_this_nr]).value_counts()

	j = 0
	for element in this_nr.index:
		# print(element[0],this_nr.array[j])

		if element[0] in otos_lotto_szamok:
			otos_lotto_szamok[element[0]] += this_nr.array[j]
		else:
			otos_lotto_szamok[element[0]] = this_nr.array[j]

		j += 1

srt_dct = sorted(otos_lotto_szamok.items())
# print(srt_dct)
# print(otos_lotto_szamok)

for i in range(1, 91):
	otos_lotto_szamok_count.append(otos_lotto_szamok[i])
	otos_lotto_szamok_list.append(i)

d = {"Nrs": otos_lotto_szamok_list, "Count": otos_lotto_szamok_count}
otos_sum = pd.DataFrame(data=d)

print(otos_sum)

# Text for the x axis
plt.xlabel("List of Numbers (1-90)")
# Text for the y axis
plt.ylabel("Number of occurrences")
# Title of the plot
plt.title("Otos Lotto Szamok")
# Plotting
plt.plot(otos_lotto_szamok_count, "-", label="Counts", linewidth=2, color="orange")
# Create the legend for the figure
plt.legend()
# Save the file
# plt.savefig('images/jpgImageDir/line_plot_' + current_time_abbrev + '.jpg', dpi=300)
# Show the file
plt.show()
