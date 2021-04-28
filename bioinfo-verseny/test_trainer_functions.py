def GeneralSlicer(incoming_filtered_dict, conditions, type="simple"):
	collecing_dict = {}
	collecting_array = []
	filtered_dict = {}

	for this_df in incoming_filtered_dict.items():

		for col_name in conditions:

			filtered_dict[col_name] = {}
			collecing_dict = {}

			for condition_value in conditions[col_name]:

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
					len(filtered_dict[col_name][condition_value]["pfs_0"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["pfs_0"]['PFS_time_months'].mean()),
					len(filtered_dict[col_name][condition_value]["pfs_1"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["pfs_1"]['PFS_time_months'].mean()),
					'{:.2f}'.format(collecing_dict[pfs_col_name] if collecing_dict[pfs_col_name] != "NaN" else 0),
					len(filtered_dict[col_name][condition_value]["dss_0"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["dss_0"]['PFS_time_months'].mean()),
					len(filtered_dict[col_name][condition_value]["dss_1"].index),
					'{:.2f}'.format(filtered_dict[col_name][condition_value]["dss_1"]['PFS_time_months'].mean()),
					'{:.2f}'.format(collecing_dict[dds_col_name] if collecing_dict[dds_col_name] != "NaN" else 0)]

				collecting_array.append(this_row)

	export_df = pd.DataFrame(data=collecting_array)
	export_df.columns = ["type", "condition", "condition_value", "pfs_0", "pfs_0_months", "pfs_1", "pfs_1_months",
						 "pfs_1_perc", "dss_0", "dss_0_months", "dss_1", "dss_1_months", "dss_1_perc"]

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
			(export_df[col_name] == iter_grade[1][col_name]) & (export_df['type'] == pair_name)]

		for iter_pair in this_grading.iterrows():
			iter_pair[1]["dss_1_perc"]

		if pair_name != "":
			this_grading2 = export_df.loc[
				(export_df[col_name] == iter_grade[1][col_name]) & (export_df['type'] == pair_name2)]

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
	filtered_export_df = export_df[
		(export_df["proportion_val_1_pfs"] < 0.9) & (export_df["proportion_val_1_pfs_chi2_p"] < 0.05)]

	if len(filtered_export_df) > 0:
		for row in export_df.iterrows():
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

			add_new_column_5.append(this_row_str)
		export_df["significance"] = add_new_column_5

	# Export file to a csv
	if type == "simple":
		filename = "data/train_grading_simple.csv"
	else:
		filename = "data/train_grading_" + type + ".csv"

	export_df.to_csv(filename, index=False)


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
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_1_PFS'] if grading_dict[this_df[
																							 0] + 'Grade_1_PFS'] != "NaN" else 0),
				len(filtered_grade1_dss_0.index),
				'{:.2f}'.format(filtered_grade1_dss_0['PFS_time_months'].mean()),
				len(filtered_grade1_dss_1.index),
				'{:.2f}'.format(filtered_grade1_dss_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_1_DSS'] if grading_dict[this_df[
																							 0] + 'Grade_1_DSS'] != "NaN" else 0)]

			this_row2 = [
				this_df[0],
				2,
				len(filtered_grade2_pfs_0.index),
				'{:.2f}'.format(filtered_grade2_pfs_0['PFS_time_months'].mean()),
				len(filtered_grade2_pfs_1.index),
				'{:.2f}'.format(filtered_grade2_pfs_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_2_PFS'] if grading_dict[this_df[
																							 0] + 'Grade_2_PFS'] != "NaN" else 0),
				len(filtered_grade2_dss_0.index),
				'{:.2f}'.format(filtered_grade2_dss_0['PFS_time_months'].mean()),
				len(filtered_grade2_dss_1.index),
				'{:.2f}'.format(filtered_grade2_dss_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_2_DSS'] if grading_dict[this_df[
																							 0] + 'Grade_2_DSS'] != "NaN" else 0)]

			this_row3 = [
				this_df[0],
				3,
				len(filtered_grade3_pfs_0.index),
				'{:.2f}'.format(filtered_grade3_pfs_0['PFS_time_months'].mean()),
				len(filtered_grade3_pfs_1.index),
				'{:.2f}'.format(filtered_grade3_pfs_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_3_PFS'] if grading_dict[this_df[
																							 0] + 'Grade_3_PFS'] != "NaN" else 0),
				len(filtered_grade3_dss_0.index),
				'{:.2f}'.format(filtered_grade3_dss_0['PFS_time_months'].mean()),
				len(filtered_grade3_dss_1.index),
				'{:.2f}'.format(filtered_grade3_dss_1['PFS_time_months'].mean()),
				'{:.2f}'.format(grading_dict[this_df[0] + 'Grade_3_DSS'] if grading_dict[this_df[
																							 0] + 'Grade_3_DSS'] != "NaN" else 0)]

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
			if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair[1]["pfs_1_perc"] == "NaN" or float(
					iter_pair[1]["pfs_1_perc"]) < 1:
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

			if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair[1]["dss_1_perc"] == "NaN" or float(
					iter_pair[1]["dss_1_perc"]) < 1:
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
			if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair[1]["pfs_1_perc"] == "NaN" or float(
					iter_grade[1]["pfs_1_perc"]) < 1:
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

			if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair[1]["dss_1_perc"] == "NaN" or float(
					iter_grade[1]["dss_1_perc"]) < 1:
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

				if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair2[1]["pfs_1_perc"] == "NaN" or float(
						iter_pair2[1]["pfs_1_perc"]) < 1:
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

				if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair2[1]["dss_1_perc"] == "NaN" or float(
						iter_pair2[1]["dss_1_perc"]) < 1:
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
				if iter_grade[1]["pfs_1_perc"] == "NaN" or iter_pair2[1]["pfs_1_perc"] == "NaN" or float(
						iter_grade[1]["pfs_1_perc"]) < 1:
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

				if iter_grade[1]["dss_1_perc"] == "NaN" or iter_pair2[1]["dss_1_perc"] == "NaN" or float(
						iter_grade[1]["dss_1_perc"]) < 1:
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

	filtered_grading = grading[
		(grading["proportion_val_1_pfs"] < 0.9) & (grading["proportion_val_1_pfs_chi2_p"] < 0.05)]

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
