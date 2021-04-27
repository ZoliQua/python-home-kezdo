#
# Semmelweis Bioinformatika verseny pályázat
#
# Készítette: Dr. Dul Zoltán, PhD
# 				a Semmelweis EMK MSc képzésének másodéves hallgatója
#

import pandas as pd
from scipy.stats import chi2_contingency


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

###########################
######### FUNCTIONS #######
###########################


def PrintChiSq(test_array, name, col_name, row_name):
	chi2, p, dof, ex = chi2_contingency(test_array, correction=False)
	print(f"")
	print(f"=" * 30)
	print(f"Chi Squre test for", name)
	print(f"=" * 30)
	if len(test_array[0]) == 2:
		print(f"\t\t\t{col_name}_0\t{col_name}_1")
	else:
		extra = "\t\t"
		for j in range(0, len(test_array[0])):
			extra += "\t" + col_name + "_" + str(j)
		print(extra)
	print(f"{row_name}_0:\t\t{test_array[0]}")
	print(f"{row_name}_1:\t\t{test_array[1]}")
	print(f"")
	print(f"Chi2-val:\t{chi2}")
	print(f"P-value:\t{'{:.8f}'.format(p)}\t{'Significant (p<0.05)' if p < 0.05 else 'NOT significant (p>0.05)'}")
	print(f"")


def ChiSqTest(retrieve_chi2):

	isZero = False

	for sublist in retrieve_chi2:
		for item in sublist:
			if item <= 0:
				isZero = True

	if not isZero:
		chi2, p, dof, ex = chi2_contingency(retrieve_chi2, correction=False)
		return p
	else:
		return 100


def Grading(incoming_filtered_dict, type="simple"):

	grading_dict = {}
	grading_multi_array = []

	for this_df in incoming_filtered_dict.items():
		filtered_grade1 = this_df[1].loc[this_df[1]['grade'] == 1]
		filtered_grade1_pfs_0 = filtered_grade1.loc[filtered_grade1['PFS_event'] == 0]
		filtered_grade1_pfs_1 = filtered_grade1.loc[filtered_grade1['PFS_event'] == 1]
		filtered_grade1_dss_0 = filtered_grade1.loc[filtered_grade1['DSS_event'] == 0]
		filtered_grade1_dss_1 = filtered_grade1.loc[filtered_grade1['DSS_event'] == 1]
		filtered_grade2 = this_df[1].loc[this_df[1]['grade'] == 2]
		filtered_grade2_pfs_0 = filtered_grade2.loc[filtered_grade2['PFS_event'] == 0]
		filtered_grade2_pfs_1 = filtered_grade2.loc[filtered_grade2['PFS_event'] == 1]
		filtered_grade2_dss_0 = filtered_grade2.loc[filtered_grade2['DSS_event'] == 0]
		filtered_grade2_dss_1 = filtered_grade2.loc[filtered_grade2['DSS_event'] == 1]
		filtered_grade3 = this_df[1].loc[this_df[1]['grade'] == 3]
		filtered_grade3_pfs_0 = filtered_grade3.loc[filtered_grade3['PFS_event'] == 0]
		filtered_grade3_pfs_1 = filtered_grade3.loc[filtered_grade3['PFS_event'] == 1]
		filtered_grade3_dss_0 = filtered_grade3.loc[filtered_grade3['DSS_event'] == 0]
		filtered_grade3_dss_1 = filtered_grade3.loc[filtered_grade3['DSS_event'] == 1]

		if len(filtered_grade1_pfs_1.index) > 0 and len(filtered_grade1_pfs_0.index) > 0:
			grading_dict[this_df[0] + "Grade_1_PFS"] = (len(filtered_grade1_pfs_1.index) * 100) / (
				len(filtered_grade1_pfs_0.index) + len(filtered_grade1_pfs_1.index))
		else:
			grading_dict[this_df[0] + "Grade_1_PFS"] = float("NaN")

		if len(filtered_grade2_pfs_1.index) > 0 and len(filtered_grade2_pfs_0.index) > 0:
			grading_dict[this_df[0] + "Grade_2_PFS"] = (len(filtered_grade2_pfs_1.index) * 100) / (
				len(filtered_grade2_pfs_0.index) + len(filtered_grade2_pfs_1.index))
		else:
			grading_dict[this_df[0] + "Grade_2_PFS"] = float("NaN")

		if len(filtered_grade3_pfs_1.index) > 0 and len(filtered_grade3_pfs_0.index) > 0:
			grading_dict[this_df[0] + "Grade_3_PFS"] = (len(filtered_grade3_pfs_1.index) * 100) / (
				len(filtered_grade3_pfs_0.index) + len(filtered_grade3_pfs_1.index))
		else:
			grading_dict[this_df[0] + "Grade_3_PFS"] = float("NaN")



		if len(filtered_grade1_dss_1.index) > 0 and len(filtered_grade1_dss_0.index) > 0:
			grading_dict[this_df[0] + "Grade_1_DSS"] = (len(filtered_grade1_dss_1.index) * 100) / (
				len(filtered_grade1_dss_0.index) + len(filtered_grade1_dss_1.index))
		else:
			grading_dict[this_df[0] + "Grade_1_DSS"] = float("NaN")

		if len(filtered_grade2_dss_1.index) > 0 and len(filtered_grade2_dss_0.index) > 0:
			grading_dict[this_df[0] + "Grade_2_DSS"] = (len(filtered_grade2_dss_1.index) * 100) / (
				len(filtered_grade2_dss_0.index) + len(filtered_grade2_dss_1.index))
		else:
			grading_dict[this_df[0] + "Grade_2_DSS"] = float("NaN")

		if len(filtered_grade3_dss_1.index) > 0 and len(filtered_grade3_dss_0.index) > 0:
			grading_dict[this_df[0] + "Grade_3_DSS"] = (len(filtered_grade3_dss_1.index) * 100) / (
				len(filtered_grade3_dss_0.index) + len(filtered_grade3_dss_1.index))
		else:
			grading_dict[this_df[0] + "Grade_3_DSS"] = float("NaN")

		if isPrintGeneralStaging:
			this_row1 = [
				this_df[0],
				1,
				len(filtered_grade1_pfs_0.index),
				'{:.2f}'.format(filtered_grade1_pfs_0['PFS_time_months'].mean()),
				len(filtered_grade1_pfs_1.index),
				'{:.2f}'.format(filtered_grade1_pfs_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_1_PFS'] if grading_dict[this_df[0] + 'Grade_1_PFS'] != "NaN" else 0),
				len(filtered_grade1_dss_0.index),
				'{:.2f}'.format(filtered_grade1_dss_0['PFS_time_months'].mean()),
				len(filtered_grade1_dss_1.index),
				'{:.2f}'.format(filtered_grade1_dss_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_1_DSS'] if grading_dict[this_df[0] + 'Grade_1_DSS'] != "NaN" else 0)]

			this_row2 = [
				this_df[0],
				2,
				len(filtered_grade2_pfs_0.index),
				'{:.2f}'.format(filtered_grade2_pfs_0['PFS_time_months'].mean()),
				len(filtered_grade2_pfs_1.index),
				'{:.2f}'.format(filtered_grade2_pfs_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_2_PFS'] if grading_dict[this_df[0] + 'Grade_2_PFS'] != "NaN" else 0),
				len(filtered_grade2_dss_0.index),
				'{:.2f}'.format(filtered_grade2_dss_0['PFS_time_months'].mean()),
				len(filtered_grade2_dss_1.index),
				'{:.2f}'.format(filtered_grade2_dss_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_2_DSS'] if grading_dict[this_df[0] + 'Grade_2_DSS'] != "NaN" else 0)]

			this_row3 = [
				this_df[0],
				3,
				len(filtered_grade3_pfs_0.index),
				'{:.2f}'.format(filtered_grade3_pfs_0['PFS_time_months'].mean()),
				len(filtered_grade3_pfs_1.index),
				'{:.2f}'.format(filtered_grade3_pfs_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_3_PFS'] if grading_dict[this_df[0] + 'Grade_3_PFS'] != "NaN" else 0),
				len(filtered_grade3_dss_0.index),
				'{:.2f}'.format(filtered_grade3_dss_0['PFS_time_months'].mean()),
				len(filtered_grade3_dss_1.index),
				'{:.2f}'.format(filtered_grade3_dss_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_3_DSS'] if grading_dict[this_df[0] + 'Grade_3_DSS'] != "NaN" else 0)]

			grading_multi_array.append(this_row1)
			grading_multi_array.append(this_row2)
			grading_multi_array.append(this_row3)

	grading = pd.DataFrame(data=grading_multi_array)
	grading.columns = ["type", "grade", "pfs_0", "pfs_0_months", "pfs_1", "pfs_1_months", "pfs_1_perc", "dss_0",
					   "dss_0_months", "dss_1", "dss_1_months", "dss_1_perc"]

	grading_new_column_1 = []
	grading_new_column_1b = []
	grading_new_column_2 = []
	grading_new_column_2b = []
	grading_new_column_3 = []
	grading_new_column_3b = []
	grading_new_column_4 = []
	grading_new_column_4b = []

	for iter_grade in grading.iterrows():

		pair_name2 = ""

		if int(iter_grade[1]["type"][-1]) == 1 and len(iter_grade[1]["type"]) < 10:
			pair_name = iter_grade[1]["type"][:-1] + "0"
			whichBigger = "iter"
		elif int(iter_grade[1]["type"][-1]) == 0 and len(iter_grade[1]["type"]) < 10:
			pair_name = iter_grade[1]["type"][:-1] + "1"
			whichBigger = "pair"
		else:
			if int(iter_grade[1]["type"][6]) == 1:
				pair_name = iter_grade[1]["type"][0:6] + str(0) + iter_grade[1]["type"][7:]
				whichBigger = "iter"
			else:
				pair_name = iter_grade[1]["type"][0:6] + str(1) + iter_grade[1]["type"][7:]
				whichBigger = "pair"

			if int(iter_grade[1]["type"][-1]) == 1:
				pair_name2 = iter_grade[1]["type"][:-1] + "0"
			else:
				pair_name2 = iter_grade[1]["type"][:-1] + "1"

		this_grading = grading.loc[(grading['grade'] == iter_grade[1]["grade"]) & (grading['type'] == pair_name)]

		for iter_pair in this_grading.iterrows():
			iter_pair[1]["dss_1_perc"]

		if pair_name != "":
			this_grading2 = grading.loc[(grading['grade'] == iter_grade[1]["grade"]) & (grading['type'] == pair_name2)]

			for iter_pair2 in this_grading2.iterrows():
				iter_pair2[1]["dss_1_perc"]

		if whichBigger == "iter":
			if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair[1]["pfs_1_perc"] == "NaN" or float(iter_pair[1]["pfs_1_perc"]) < 1:
				grading_new_column_1.append(float("NaN"))
				grading_new_column_1b.append(float("NaN"))
			else:
				grading_new_column_1.append(
					float('{:.4f}'.format(float(iter_grade[1]["pfs_1_perc"]) / float(iter_pair[1]["pfs_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
								 [iter_pair[1]["pfs_0"], iter_pair[1]["pfs_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					grading_new_column_1b.append(float('{:.6f}'.format(float(p_val))))
				else:
					grading_new_column_1b.append(float("NaN"))

			if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair[1]["dss_1_perc"] == "NaN" or float(iter_pair[1]["dss_1_perc"]) < 1:
				grading_new_column_3.append(float("NaN"))
				grading_new_column_3b.append(float("NaN"))
			else:
				grading_new_column_3.append(
					float('{:.4f}'.format(float(iter_grade[1]["dss_1_perc"]) / float(iter_pair[1]["dss_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
								 [iter_pair[1]["dss_0"], iter_pair[1]["dss_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					grading_new_column_3b.append(float('{:.6f}'.format(float(p_val))))
				else:
					grading_new_column_3b.append(float("NaN"))

		else:
			if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair[1]["pfs_1_perc"] == "NaN" or float(iter_grade[1]["pfs_1_perc"]) < 1:
				grading_new_column_1.append(float("NaN"))
				grading_new_column_1b.append(float("NaN"))
			else:
				grading_new_column_1.append(
					float('{:.4f}'.format(float(iter_pair[1]["pfs_1_perc"]) / float(iter_grade[1]["pfs_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
								 [iter_pair[1]["pfs_0"], iter_pair[1]["pfs_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					grading_new_column_1b.append(float('{:.6f}'.format(float(p_val))))
				else:
					grading_new_column_1b.append(float("NaN"))

			if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair[1]["dss_1_perc"] == "NaN" or float(iter_grade[1]["dss_1_perc"]) < 1:
				grading_new_column_3.append(float("NaN"))
				grading_new_column_3b.append(float("NaN"))
			else:
				grading_new_column_3.append(
					float('{:.4f}'.format(float(iter_pair[1]["dss_1_perc"]) / float(iter_grade[1]["dss_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
								 [iter_pair[1]["dss_0"], iter_pair[1]["dss_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					grading_new_column_3b.append(float('{:.6f}'.format(float(p_val))))
				else:
					grading_new_column_3b.append(float("NaN"))

		if len(iter_grade[1]["type"]) > 9:
			if int(iter_grade[1]["type"][-1]) == 1:

				if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair2[1]["pfs_1_perc"] == "NaN" or float(iter_pair2[1]["pfs_1_perc"]) < 1:
					grading_new_column_2.append(float("NaN"))
					grading_new_column_2b.append(float("NaN"))
				else:
					grading_new_column_2.append(
						float('{:.4f}'.format(float(iter_grade[1]["pfs_1_perc"]) / float(iter_pair2[1]["pfs_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
									 [iter_pair2[1]["pfs_0"], iter_pair2[1]["pfs_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						grading_new_column_2b.append(float('{:.6f}'.format(float(p_val))))
					else:
						grading_new_column_2b.append(float("NaN"))

				if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair2[1]["dss_1_perc"] == "NaN" or float(iter_pair2[1]["dss_1_perc"]) < 1:
					grading_new_column_4.append(float("NaN"))
					grading_new_column_4b.append(float("NaN"))
				else:
					grading_new_column_4.append(
						float('{:.4f}'.format(float(iter_grade[1]["dss_1_perc"]) / float(iter_pair2[1]["dss_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
									 [iter_pair2[1]["dss_0"], iter_pair2[1]["dss_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						grading_new_column_4b.append(float('{:.6f}'.format(float(p_val))))
					else:
						grading_new_column_4b.append(float("NaN"))

			else:
				if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair2[1]["pfs_1_perc"] == "NaN" or float(iter_grade[1]["pfs_1_perc"]) < 1:
					grading_new_column_2.append(float("NaN"))
					grading_new_column_2b.append(float("NaN"))
				else:
					grading_new_column_2.append(
						float('{:.4f}'.format(float(iter_pair2[1]["pfs_1_perc"]) / float(iter_grade[1]["pfs_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
									 [iter_pair2[1]["pfs_0"], iter_pair2[1]["pfs_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						grading_new_column_2b.append(float('{:.6f}'.format(float(p_val))))
					else:
						grading_new_column_2b.append(float("NaN"))

				if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair2[1]["dss_1_perc"] == "NaN" or float(iter_grade[1]["dss_1_perc"]) < 1:
					grading_new_column_4.append(float("NaN"))
					grading_new_column_4b.append(float("NaN"))
				else:
					grading_new_column_4.append(
						float('{:.4f}'.format(float(iter_pair2[1]["dss_1_perc"]) / float(iter_grade[1]["dss_1_perc"]))))


					retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
									 [iter_pair2[1]["dss_0"], iter_pair2[1]["dss_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						grading_new_column_4b.append(float('{:.6f}'.format(float(p_val))))
					else:
						grading_new_column_4b.append(float("NaN"))

		else:
			grading_new_column_2.append(float("NaN"))
			grading_new_column_2b.append(float("NaN"))
			grading_new_column_4.append(float("NaN"))
			grading_new_column_4b.append(float("NaN"))

	grading["proportion_val_1_pfs"] = grading_new_column_1
	grading["proportion_val_1_pfs_chi2_p"] = grading_new_column_1b
	grading["proportion_val_2_pfs"] = grading_new_column_2
	grading["proportion_val_2_pfs_chi2_p"] = grading_new_column_2b
	grading["proportion_val_1_dds"] = grading_new_column_3
	grading["proportion_val_1_dds_chi2_p"] = grading_new_column_3b
	grading["proportion_val_2_dds"] = grading_new_column_4
	grading["proportion_val_2_dds_chi2_p"] = grading_new_column_4b

	grading.astype({"proportion_val_1_pfs": 'float'}).dtypes
	grading.astype({"proportion_val_1_pfs_chi2_p": 'float'}).dtypes


	filtered_grading = grading[(grading["proportion_val_1_pfs"] < 0.9) & (grading["proportion_val_1_pfs_chi2_p"] < 0.05)]

	grading_new_column_5 = []

	if len(filtered_grading) > 0:
		for row in grading.iterrows():
			this_row = []
			if row[1]["proportion_val_1_pfs"] < 0.9 and row[1]["proportion_val_1_pfs_chi2_p"] < 0.05:
				this_row.append("PFS (p<0.05)")
			if row[1]["proportion_val_2_pfs"] < 0.9 and row[1]["proportion_val_2_pfs_chi2_p"] < 0.05:
				this_row.append("PFS 2nd (p<0.05)")
			if row[1]["proportion_val_1_dds"] < 0.9 and row[1]["proportion_val_1_dds_chi2_p"] < 0.05:
				this_row.append("DDS (p<0.05)")
			if row[1]["proportion_val_2_dds"] < 0.9 and row[1]["proportion_val_2_dds_chi2_p"] < 0.05:
				this_row.append("DDS (p<0.05)")
			this_row_str = ", ".join(this_row)

			grading_new_column_5.append(this_row_str)

		grading["significiance"] = grading_new_column_5


	if type == "simple":
		filename = "data/train_grading_simple.csv"
	else:
		filename = "data/train_grading_" + type + ".csv"

	grading.to_csv(filename, index=False)


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

Grading(filtered_dict)

# Age slicing

# age_range = [(1, 40), (41, 55), (56, 70), (71, 100)]
age_range = [(1, 50), (51, 65), (66, 100)]

for this_range in age_range:

	name = "age_" + str(this_range[0]).zfill(2) + "_" + str(this_range[1]).zfill(2)
	filtered_dict_by_age = {}

	for this_df in filtered_dict.items():
		filtered_dict_by_age[this_df[0]] = this_df[1][ (this_df[1]["age_at_diagnosis"] >= this_range[0]) & (this_df[1]["age_at_diagnosis"] <= this_range[1]) ]

	Grading(filtered_dict_by_age, name)

# filtered_by_age = df[(df['age_at_diagnosis']>=99 ) & (df['closing_price']<=101)]


# for this_df in filtered_dict.items():
# 	filtered_pfs1 = this_df[1].loc[this_df[1]['PFS_event'] == 1]
# 	print(f"{this_df[0]} =>\tRows: {len(filtered_pfs1.index)}\tAverage (mean): {'{:.4f}'.format(filtered_pfs1['PFS_time_months'].mean())} ")

# filtered.to_csv("data/train_export.csv", index=False)


