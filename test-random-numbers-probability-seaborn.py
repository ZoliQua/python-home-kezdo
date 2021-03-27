#
# In this file I tested random generators and plotting in matplotlib, seaborn lib
#

from datetime import datetime
import numpy as np

#
# Importing MatPlotLib
#

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#
# Here comes the code
#

w = np.array([ 0.4,  0.8,  2.6,  1.8,  0.2, 1])
dct = {0.4: 0,  0.8: 0,  2.6: 0,  1.8: 0,  0.2: 0, 1: 0}

for i in range(1,10000):
	selected = np.random.choice(w, p=w/sum(w))
	dct[selected] += 1

sumnum = 0
sumnum_key = 0
for dict_key in dct:
	sumnum += dct[dict_key]
	sumnum_key += dict_key

# dct_sorted = dict( sorted(dct.items(), key = lambda item: item[1]) )
# print(dct_sorted)

dct_sorted = dict( sorted( dct.items() ) )
print(dct_sorted)

for dict_key in dct_sorted:
	percent = "{:.4f}%".format( (dct[dict_key]/sumnum) * 100 )
	percent_key = "{:.4f}%".format( (dict_key/sumnum_key) * 100 )
	print(f"{dict_key} ({percent_key}): {dct[dict_key]} ({percent})")

print(dct)


# Plotting

plt.figure(figsize=(10, 7))
df = pd.DataFrame({"Keys": dct_sorted.keys(), "Values": dct_sorted.values()})

sns.color_palette("pastel")
splot = sns.barplot(x="Keys", y="Values", data=df, palette="Set2")

for p in splot.patches:
	# Original source
	# text = format(p.get_height(), '.0f')
	text = str(int(p.get_height())) + " \n(" + "{:.2f}%".format( (p.get_height()/sumnum) * 100 ) +")"
	splot.annotate(text,
						(p.get_x() + p.get_width() / 2, p.get_height()),
						ha = 'center', va = 'center',
						xytext = (0, -14),
						textcoords = 'offset points',
						fontsize = 'large',
						color = "white")

# Text for the x axis
plt.xlabel("Random probability values")
# Text for the y axis
plt.ylabel("Number of iterations")
# Title of the plot
plt.title("Random generator by probability")

# Create the legend for the figure
# plt.legend()


# Creating timestamp for output plot filename
now = datetime.now()
current_time_abbrev = now.strftime("%Y%m%d-%H%M%S-%f")
# Save the file
plt.savefig('imgages/jpgImageDir/barplot_' + current_time_abbrev + '.jpg', dpi=300)
# Show the file
plt.show()
# Print the date into the console
# print(list_of_minmax)


