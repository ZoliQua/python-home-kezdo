
import pandas as pd
import os.path
from os import path
from scipy.stats import chi2_contingency
from statistics import stdev

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


def GeneralSlicer(incoming_filtered_dict, conditions, sub_conditions, call_type="simple", write_mode="a"):
	collecing_dict = {}
	collecting_array = []
	filtered_dict = {}

	# Export file to a csv
	if call_type == "simple":
		filename = "data/train_statistics.csv"
	else:
		filename = "data/train_statistics_" + call_type + ".csv"

	isExportFileExist = path.exists(filename)

	for this_df in incoming_filtered_dict.items():

		for col_name in conditions:

			filtered_dict[col_name] = {}
			collecing_dict = {}

			for condition_value in conditions[col_name]:

				if type(condition_value) == list:

					condition_list = condition_value
					condition_value = "_".join(condition_list)

					filtered_dict[col_name][condition_value] = {}

					connecting_subset_dfs = []

					for this_cond_val in condition_list:
						connecting_subset_dfs.append(this_df[1].loc[this_df[1][col_name] == this_cond_val])

					filtered_dict[col_name][condition_value]["base"] = pd.concat(connecting_subset_dfs)

					# filtered_dict[col_name][condition_value]["base"] = this_df[1][
					#	this_df[1][col_name].str.contains(condition_value, case=False, na=False)]
					#	this_df[1][col_name].str.find(condition_value) != -1]

				else:
					filtered_dict[col_name][condition_value] = {}
					filtered_dict[col_name][condition_value]["base"] = this_df[1].loc[
						this_df[1][col_name] == condition_value]

				filtered_dict[col_name][condition_value]["pfs_0"] = \
					filtered_dict[col_name][condition_value]["base"].loc[
						filtered_dict[col_name][condition_value]["base"]['PFS_event'] == 0]

				filtered_dict[col_name][condition_value]["pfs_1"] = \
					filtered_dict[col_name][condition_value]["base"].loc[
						filtered_dict[col_name][condition_value]["base"]['PFS_event'] == 1]

				filtered_dict[col_name][condition_value]["dss_0"] = \
					filtered_dict[col_name][condition_value]["base"].loc[
						filtered_dict[col_name][condition_value]["base"]['DSS_event'] == 0]

				filtered_dict[col_name][condition_value]["dss_1"] = \
					filtered_dict[col_name][condition_value]["base"].loc[
						filtered_dict[col_name][condition_value]["base"]['DSS_event'] == 1]

				pfs_col_name = this_df[0] + "_" + col_name + "_PFS"
				dds_col_name = this_df[0] + "_" + col_name + "_DDS"

				# Determine PFS % = PFS_1 / (PFS_1 + PFS_0)
				if len(filtered_dict[col_name][condition_value]["pfs_1"].index) > 0 and len(
						filtered_dict[col_name][condition_value]["pfs_0"].index) > 0:
					collecing_dict[pfs_col_name] = (len(
						filtered_dict[col_name][condition_value]["pfs_1"].index) * 100) / (
														   len(filtered_dict[col_name][condition_value][
																   "pfs_0"].index) + len(
													   filtered_dict[col_name][condition_value]["pfs_1"].index))
				else:
					collecing_dict[pfs_col_name] = float("NaN")

				# Determine DSS % = DSS_1 / (DSS_1 + DSS_0)
				if len(filtered_dict[col_name][condition_value]["dss_1"].index) > 0 and len(
						filtered_dict[col_name][condition_value]["dss_0"].index) > 0:
					collecing_dict[dds_col_name] = (len(
						filtered_dict[col_name][condition_value]["dss_1"].index) * 100) / (
														   len(filtered_dict[col_name][condition_value][
																   "dss_0"].index) + len(
													   filtered_dict[col_name][condition_value]["dss_1"].index))
				else:
					collecing_dict[dds_col_name] = float("NaN")

				# Create this row from elements, 13 indexes
				this_row = [
					this_df[0],
					col_name,
					condition_value,
					sub_conditions["col_name"],
					sub_conditions["cond_value"],
					len(filtered_dict[col_name][condition_value]["pfs_0"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["pfs_0"]['PFS_time_months'].mean()),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["pfs_0"]['PFS_time_months'].std()),
					len(filtered_dict[col_name][condition_value]["pfs_1"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["pfs_1"]['PFS_time_months'].mean()),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["pfs_1"]['PFS_time_months'].std()),
					'{:.2f}'.format(collecing_dict[pfs_col_name] if collecing_dict[pfs_col_name] != "NaN" else 0),
					len(filtered_dict[col_name][condition_value]["dss_0"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["dss_0"]['PFS_time_months'].mean()),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["dss_0"]['PFS_time_months'].std()),
					len(filtered_dict[col_name][condition_value]["dss_1"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["dss_1"]['PFS_time_months'].mean()),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["dss_1"]['PFS_time_months'].std()),
					'{:.2f}'.format(collecing_dict[dds_col_name] if collecing_dict[dds_col_name] != "NaN" else 0)]

				collecting_array.append(this_row)

	export_df = pd.DataFrame(data=collecting_array)
	export_df.columns = ["type", "main_condition", "condition_value", "sub_condition", "sub_condition_value", "pfs_0", "pfs_0_months_mean", "pfs_0_months_std", "pfs_1", "pfs_1_months_mean",
						 "pfs_1_months_std", "pfs_1_perc", "dss_0", "dss_0_months_mean", "dss_0_months_std", "dss_1", "dss_1_months_mean",
						 "dss_1_months_std", "dss_1_perc"]

	add_new_column_1 = []
	add_new_column_1b = []
	add_new_column_2 = []
	add_new_column_2b = []
	add_new_column_3 = []
	add_new_column_3b = []
	add_new_column_4 = []
	add_new_column_4b = []

	for iter_grade in export_df.iterrows():

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

		this_grading = export_df.loc[
			(export_df["condition_value"] == iter_grade[1]["condition_value"]) & (export_df['type'] == pair_name)]

		for iter_pair in this_grading.iterrows():
			iter_pair[1]["dss_1_perc"]

		if pair_name != "":
			this_grading2 = export_df.loc[
				(export_df["condition_value"] == iter_grade[1]["condition_value"]) & (export_df['type'] == pair_name2)]

			for iter_pair2 in this_grading2.iterrows():
				iter_pair2[1]["dss_1_perc"]

		if whichBigger == "iter":
			if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair[1]["pfs_1_perc"] == "NaN" or float(
					iter_pair[1]["pfs_1_perc"]) < 1:
				add_new_column_1.append(float("NaN"))
				add_new_column_1b.append(float("NaN"))
			else:
				add_new_column_1.append(
					float('{:.4f}'.format(float(iter_grade[1]["pfs_1_perc"]) / float(iter_pair[1]["pfs_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
								 [iter_pair[1]["pfs_0"], iter_pair[1]["pfs_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					add_new_column_1b.append(float('{:.6f}'.format(float(p_val))))
				else:
					add_new_column_1b.append(float("NaN"))

			if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair[1]["dss_1_perc"] == "NaN" or float(
					iter_pair[1]["dss_1_perc"]) < 1:
				add_new_column_3.append(float("NaN"))
				add_new_column_3b.append(float("NaN"))
			else:
				add_new_column_3.append(
					float('{:.4f}'.format(float(iter_grade[1]["dss_1_perc"]) / float(iter_pair[1]["dss_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
								 [iter_pair[1]["dss_0"], iter_pair[1]["dss_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					add_new_column_3b.append(float('{:.6f}'.format(float(p_val))))
				else:
					add_new_column_3b.append(float("NaN"))

		else:
			if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair[1]["pfs_1_perc"] == "NaN" or float(
					iter_grade[1]["pfs_1_perc"]) < 1:
				add_new_column_1.append(float("NaN"))
				add_new_column_1b.append(float("NaN"))
			else:
				add_new_column_1.append(
					float('{:.4f}'.format(float(iter_pair[1]["pfs_1_perc"]) / float(iter_grade[1]["pfs_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
								 [iter_pair[1]["pfs_0"], iter_pair[1]["pfs_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					add_new_column_1b.append(float('{:.6f}'.format(float(p_val))))
				else:
					add_new_column_1b.append(float("NaN"))

			if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair[1]["dss_1_perc"] == "NaN" or float(
					iter_grade[1]["dss_1_perc"]) < 1:
				add_new_column_3.append(float("NaN"))
				add_new_column_3b.append(float("NaN"))
			else:
				add_new_column_3.append(
					float('{:.4f}'.format(float(iter_pair[1]["dss_1_perc"]) / float(iter_grade[1]["dss_1_perc"]))))

				retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
								 [iter_pair[1]["dss_0"], iter_pair[1]["dss_1"]]]

				p_val = ChiSqTest(retrieve_chi2)
				if p_val != 100:
					add_new_column_3b.append(float('{:.6f}'.format(float(p_val))))
				else:
					add_new_column_3b.append(float("NaN"))

		if len(iter_grade[1]["type"]) > 9:
			if int(iter_grade[1]["type"][-1]) == 1:

				if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair2[1]["pfs_1_perc"] == "NaN" or float(
						iter_pair2[1]["pfs_1_perc"]) < 1:
					add_new_column_2.append(float("NaN"))
					add_new_column_2b.append(float("NaN"))
				else:
					add_new_column_2.append(
						float('{:.4f}'.format(float(iter_grade[1]["pfs_1_perc"]) / float(iter_pair2[1]["pfs_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
									 [iter_pair2[1]["pfs_0"], iter_pair2[1]["pfs_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						add_new_column_2b.append(float('{:.6f}'.format(float(p_val))))
					else:
						add_new_column_2b.append(float("NaN"))

				if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair2[1]["dss_1_perc"] == "NaN" or float(
						iter_pair2[1]["dss_1_perc"]) < 1:
					add_new_column_4.append(float("NaN"))
					add_new_column_4b.append(float("NaN"))
				else:
					add_new_column_4.append(
						float('{:.4f}'.format(float(iter_grade[1]["dss_1_perc"]) / float(iter_pair2[1]["dss_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
									 [iter_pair2[1]["dss_0"], iter_pair2[1]["dss_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						add_new_column_4b.append(float('{:.6f}'.format(float(p_val))))
					else:
						add_new_column_4b.append(float("NaN"))

			else:
				if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair2[1]["pfs_1_perc"] == "NaN" or float(
						iter_grade[1]["pfs_1_perc"]) < 1:
					add_new_column_2.append(float("NaN"))
					add_new_column_2b.append(float("NaN"))
				else:
					add_new_column_2.append(
						float('{:.4f}'.format(float(iter_pair2[1]["pfs_1_perc"]) / float(iter_grade[1]["pfs_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["pfs_0"], iter_grade[1]["pfs_1"]],
									 [iter_pair2[1]["pfs_0"], iter_pair2[1]["pfs_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						add_new_column_2b.append(float('{:.6f}'.format(float(p_val))))
					else:
						add_new_column_2b.append(float("NaN"))

				if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair2[1]["dss_1_perc"] == "NaN" or float(
						iter_grade[1]["dss_1_perc"]) < 1:
					add_new_column_4.append(float("NaN"))
					add_new_column_4b.append(float("NaN"))
				else:
					add_new_column_4.append(
						float('{:.4f}'.format(float(iter_pair2[1]["dss_1_perc"]) / float(iter_grade[1]["dss_1_perc"]))))

					retrieve_chi2 = [[iter_grade[1]["dss_0"], iter_grade[1]["dss_1"]],
									 [iter_pair2[1]["dss_0"], iter_pair2[1]["dss_1"]]]

					p_val = ChiSqTest(retrieve_chi2)
					if p_val != 100:
						add_new_column_4b.append(float('{:.6f}'.format(float(p_val))))
					else:
						add_new_column_4b.append(float("NaN"))

		else:
			add_new_column_2.append(float("NaN"))
			add_new_column_2b.append(float("NaN"))
			add_new_column_4.append(float("NaN"))
			add_new_column_4b.append(float("NaN"))

	export_df["proportion_val_1_pfs"] = add_new_column_1
	export_df["proportion_val_1_pfs_chi2_p"] = add_new_column_1b
	export_df["proportion_val_2_pfs"] = add_new_column_2
	export_df["proportion_val_2_pfs_chi2_p"] = add_new_column_2b
	export_df["proportion_val_1_dds"] = add_new_column_3
	export_df["proportion_val_1_dds_chi2_p"] = add_new_column_3b
	export_df["proportion_val_2_dds"] = add_new_column_4
	export_df["proportion_val_2_dds_chi2_p"] = add_new_column_4b

	export_df.astype({"proportion_val_1_pfs": 'float'}).dtypes
	export_df.astype({"proportion_val_1_pfs_chi2_p": 'float'}).dtypes

	# Filtering export_df to determine, whether there is any significance of the row
	add_new_column_5 = []
	add_new_column_6 = []
	filtered_export_df = export_df[
		(export_df["proportion_val_1_pfs"] < 0.9) & (export_df["proportion_val_1_pfs_chi2_p"] < 0.05)]

	if len(filtered_export_df) > 0:
		for row in export_df.iterrows():
			this_row = []
			this_value = 0
			if row[1]["proportion_val_1_pfs"] < 0.9 and row[1]["proportion_val_1_pfs_chi2_p"] < 0.05:
				this_row.append("PFS (p<0.05)")
				this_value = 1
			if row[1]["proportion_val_2_pfs"] < 0.9 and row[1]["proportion_val_2_pfs_chi2_p"] < 0.05:
				this_row.append("PFS 2nd (p<0.05)")
				this_value = 1
			if row[1]["proportion_val_1_dds"] < 0.9 and row[1]["proportion_val_1_dds_chi2_p"] < 0.05:
				this_row.append("DDS (p<0.05)")
				this_value = 1
			if row[1]["proportion_val_2_dds"] < 0.9 and row[1]["proportion_val_2_dds_chi2_p"] < 0.05:
				this_row.append("DDS (p<0.05)")
				this_value = 1
			this_row_str = ", ".join(this_row)

			add_new_column_5.append(this_row_str)
			add_new_column_6.append(this_value)

		export_df["significance_level"] = add_new_column_5
		export_df["significance"] = add_new_column_6

	# Write export file inta a csv file using pandas export "to_csv" function
	if not isExportFileExist:
		export_df.to_csv(filename, index=False, mode=write_mode)
	else:
		export_df.to_csv(filename, index=False, header=False, mode=write_mode)


