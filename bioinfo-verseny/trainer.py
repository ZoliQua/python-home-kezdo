#
# Semmelweis Bioinformatika verseny pályázat
#
# Készítette: Dr. Dul Zoltán, PhD
# 				a Semmelweis EMK MSc képzésének másodéves hallgatója
#

from trainer_functions import *


###########################
####### GENERAL DEF #######
###########################

# To Print General statistics
isPrintGeneralStat = False
# To Print PFS statistics
isPrintPFSStat = False
isPrintGeneralStaging = True
# To Print Any ChiSq test
isPrintChiSq = False

# Load the train data into pandas dataframe
mydata = pd.read_csv("data/train.csv")

# Filter the dataframe, and drop rows with NA in 'adjuvant_chemotherapy' and 'hormone_therapy' columns
df = mydata.dropna(subset=['adjuvant_chemotherapy', 'hormone_therapy'])

# Slice the dataframe into four subsets, based on the usage of chemotherapy and hormone therapy
filtered_ch0_ho0 = df.loc[(df['adjuvant_chemotherapy'] == 0) & (df['hormone_therapy'] == 0)]
filtered_ch0_ho1 = df.loc[(df['adjuvant_chemotherapy'] == 0) & (df['hormone_therapy'] == 1)]
filtered_ch1_ho0 = df.loc[(df['adjuvant_chemotherapy'] == 1) & (df['hormone_therapy'] == 0)]
filtered_ch1_ho1 = df.loc[(df['adjuvant_chemotherapy'] == 1) & (df['hormone_therapy'] == 1)]
filtered_ch0 = df.loc[(df['adjuvant_chemotherapy'] == 0)]
filtered_ch1 = df.loc[(df['adjuvant_chemotherapy'] == 1)]
filtered_ho0 = df.loc[(df['hormone_therapy'] == 0)]
filtered_ho1 = df.loc[(df['hormone_therapy'] == 1)]

# Number of rows for these therapies
rows_ch0_ho0 = len(filtered_ch0_ho0.index)
rows_ch0_ho1 = len(filtered_ch0_ho1.index)
rows_ch1_ho0 = len(filtered_ch1_ho0.index)
rows_ch1_ho1 = len(filtered_ch1_ho1.index)

# Print general information about row numbers created by the previous slicing
if isPrintGeneralStat:
	print("Row numbers, without chemo or hormontherapy:", rows_ch0_ho0)
	print("Row numbers, with hormontherapy only:", rows_ch0_ho1)
	print("Row numbers, with adj. chemotherapy only:", rows_ch1_ho0)
	print("Row numbers, with both therapy:", rows_ch1_ho1)

filtered_dict = {	"Chemo_0_Hormo_0": filtered_ch0_ho0,
					"Chemo_0_Hormo_1": filtered_ch0_ho1,
					"Chemo_1_Hormo_0": filtered_ch1_ho0,
					"Chemo_1_Hormo_1": filtered_ch1_ho1,
					"Chemo_0": filtered_ch0,
					"Chemo_1": filtered_ch1,
					"Hormon_0": filtered_ho0,
					"Hormon_1": filtered_ho1 }

#
# Testing General PFS Chemotherapy/Hormontherapy relation and significance
#

rows_pfs0 = []
rows_pfs1 = []

for this_df in filtered_dict.items():
	filtered_pfs0 = this_df[1].loc[this_df[1]['PFS_event'] == 0]
	filtered_pfs1 = this_df[1].loc[this_df[1]['PFS_event'] == 1]
	if isPrintPFSStat:
		print(f"{this_df[0]} =>\t\tPFS_0:\t{len(filtered_pfs0.index)}\t\tPFS_1:\t{len(filtered_pfs1.index)}\t\t"
		      f"SUM:\t{len(this_df[1].index)}\t\tAverage PFS time (mean): {'{:.4f}'.format(filtered_pfs0['PFS_time_months'].mean())} ")
	rows_pfs0.append(len(filtered_pfs0.index))
	rows_pfs1.append(len(filtered_pfs1.index))

# ChiSq test for Chemotherapy
kemo = [[rows_pfs0[0] + rows_pfs0[1], rows_pfs1[0] + rows_pfs1[1]], [rows_pfs0[2] + rows_pfs0[3], rows_pfs1[2] + rows_pfs1[3]]]
if isPrintChiSq:
	PrintChiSq(kemo, "Adj. Chemotherapy", "pfs", "kemo")

# ChiSq test for Adj. Hormontherapy
hormon = [[rows_pfs0[0] + rows_pfs0[2], rows_pfs1[0] + rows_pfs1[2]], [rows_pfs0[1] + rows_pfs0[3], rows_pfs1[1] + rows_pfs1[3]]]
if isPrintChiSq:
	PrintChiSq(hormon, "Hormontherapy", "pfs", "horm")

#
# Testing Grading and PFS Chemotherapy / Hormontherapy relation and significance
#

grader = {"grade": [1, 2, 3]}
# Grading(filtered_dict)
GeneralSlicer(filtered_dict, grader)

#
# Age slicing
#
# age_range = [(1, 40), (41, 55), (56, 70), (71, 100)]
age_range = [(1, 50), (51, 65), (66, 100)]

for this_range in age_range:

	name = "age_" + str(this_range[0]).zfill(2) + "_" + str(this_range[1]).zfill(2)
	filtered_dict_by_age = {}

	for this_df in filtered_dict.items():
		filtered_dict_by_age[this_df[0]] = this_df[1][ (this_df[1]["age_at_diagnosis"] >= this_range[0]) & (this_df[1]["age_at_diagnosis"] <= this_range[1]) ]

	GeneralSlicer(filtered_dict_by_age, grader, name)

# Staging filtering out
stager = {"pathologic_stage": ["I", "IA", "IB", "II", "IIA", "IIB", "III", "IIIA", "IIIB", "IIIC", "IV"]}
GeneralSlicer(filtered_dict, stager, "stage_simple")

stager = {"pathologic_stage": [["I", "IA", "IB"], ["II", "IIA", "IIB"], ["III", "IIIA", "IIIB", "IIIC"], "IV"]}
GeneralSlicer(filtered_dict, stager, "stage_combined")

# filtered_by_age = df[(df['age_at_diagnosis']>=99 ) & (df['closing_price']<=101)]


# for this_df in filtered_dict.items():
# 	filtered_pfs1 = this_df[1].loc[this_df[1]['PFS_event'] == 1]
# 	print(f"{this_df[0]} =>\tRows: {len(filtered_pfs1.index)}\tAverage (mean): {'{:.4f}'.format(filtered_pfs1['PFS_time_months'].mean())} ")

# filtered.to_csv("data/train_export.csv", index=False)


