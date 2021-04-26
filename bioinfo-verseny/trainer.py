#
# Semmelweis Bioinformatika verseny pályázat
#
# Készítette: Dr. Dul Zoltán, PhD
# 				a Semmelweis EMK MSc képzésének másodéves hallgatója
#

import pandas as pd
from scipy.stats import chi2_contingency

# Load the train data into pandas dataframe
mydata = pd.read_csv("data/train.csv")

# Filter the dataframe, and drop rows w/ NA in 'adjuvant_chemotherapy' and 'hormone_therapy'
df = mydata.dropna(subset=['adjuvant_chemotherapy', 'hormone_therapy'])

# Slice the dataframe into four subsets, based on the usage of chemotherapy and hormone therapy
filtered_ch0_th0 = df.loc[(df['adjuvant_chemotherapy'] == 0) & (df['hormone_therapy'] == 0)]
filtered_ch0_th1 = df.loc[(df['adjuvant_chemotherapy'] == 0) & (df['hormone_therapy'] == 1)]
filtered_ch1_th0 = df.loc[(df['adjuvant_chemotherapy'] == 1) & (df['hormone_therapy'] == 0)]
filtered_ch1_th1 = df.loc[(df['adjuvant_chemotherapy'] == 1) & (df['hormone_therapy'] == 1)]

# Number of rows
rows_ch0_th0 = len(filtered_ch0_th0.index)
rows_ch0_th1 = len(filtered_ch0_th1.index)
rows_ch1_th0 = len(filtered_ch1_th0.index)
rows_ch1_th1 = len(filtered_ch1_th1.index)

# Print the information about row numbers created by the previous slicing
print("Sorok száma, ahol sem adj. kemoterápia sem hormonterápia nem volt:", rows_ch0_th0)
print("Sorok száma, ahol csak hormonterápia volt:", rows_ch0_th1)
print("Sorok száma, ahol csak adj. kemoterápia volt:", rows_ch1_th0)
print("Sorok száma, ahol mindkét kezelés volt:", rows_ch1_th1)

filtered_dict = {	"Kemo 0, Hormon 0": filtered_ch0_th0,
					"Kemo 0, Hormon 1": filtered_ch0_th1,
					"Kemo 1, Hormon 0": filtered_ch1_th0,
					"Kemo 1, Hormon 1": filtered_ch1_th1 }

rows_pfs0 = []
rows_pfs1 = []

for this_df in filtered_dict.items():
	filtered_pfs0 = this_df[1].loc[this_df[1]['PFS_event'] == 0]
	print(f"{this_df[0]} =>\tRows: {len(filtered_pfs0.index)} ({len(this_df[1].index)})\t"
		  f"Average (mean): {'{:.4f}'.format(filtered_pfs0['PFS_time_months'].mean())} ")
	rows_pfs0.append(len(filtered_pfs0.index))
	rows_pfs1.append(len(this_df[1].index) - len(filtered_pfs0.index))


chi2, p, dof, ex = chi2_contingency([rows_pfs0, rows_pfs1], correction=False)

print(chi2, p)

# for this_df in filtered_dict.items():
# 	filtered_pfs1 = this_df[1].loc[this_df[1]['PFS_event'] == 1]
# 	print(f"{this_df[0]} =>\tRows: {len(filtered_pfs1.index)}\tAverage (mean): {'{:.4f}'.format(filtered_pfs1['PFS_time_months'].mean())} ")

# filtered.to_csv("data/train_export.csv", index=False)


