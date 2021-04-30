#
# Semmelweis Bioinformatika verseny pályázat
#
# Készítette: Dr. Dul Zoltán, PhD
# 				a Semmelweis EMK MSc képzésének másodéves hallgatója
#

from trainer_functions import *

# Load the train data into pandas dataframe
mydata = pd.read_csv("data/train.csv")

# Load statistics into pandas dataframe
stat = pd.read_csv("data/train_statistics.csv")
stat_significant = stat.loc[stat['significance'] == 1]

positive_list = []

for iter_item in stat_significant.iterrows():

	this_row = {}

	if iter_item[1]["type"][0:5] == "chemo":
		this_row["adjuvant_chemotherapy"] = [1]
	elif iter_item[1]["type"][0:5] == "hormo":
		this_row["hormone_therapy"] = [1]

	if (len(iter_item[1]["type"]) > 8):
		if iter_item[1]["type"][8:13] == "chemo":
			this_row["adjuvant_chemotherapy"] = [1]
		elif iter_item[1]["type"][8:13] == "hormo":
			this_row["hormone_therapy"] = [1]

	if iter_item[1]["condition_value"].count("_") > 0:
		sub_items = iter_item[1]["condition_value"].split("_")
	else:
		sub_items = [iter_item[1]["condition_value"]]

	this_row[iter_item[1]["main_condition"]] = sub_items

	if type(iter_item[1]["sub_condition"]) == str:
		sub_items = iter_item[1]["sub_condition_value"].split("_")
		this_row[iter_item[1]["sub_condition"]] = [int(sub_items[1]), int(sub_items[2])]

	positive_list.append(this_row)

list_of_sign = []

for iter_item in mydata.iterrows():

	significant = False

	for condition in positive_list:

		isBreak = False

		for cell_name in condition:

			if len(condition[cell_name]) == 1:
				if iter_item[1][cell_name] != condition[cell_name]:
					isBreak = True
					continue

		if not isBreak:
			significant = True
			list_of_sign.append(iter_item[0])

	#break
print(list_of_sign)








