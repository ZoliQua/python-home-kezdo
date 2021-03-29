import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Import dataframe using pandas
otos = pd.read_csv("data/otos.csv", sep=";", usecols=["Year","Week","Nr1","Nr2","Nr3","Nr4","Nr5"])

# # Groupping the data by "Region" and "Sales"
groupping = otos.groupby(by=["Nr1","Nr2","Nr3","Nr4","Nr5"]).max()

nr_1 = otos.groupby(by=["Nr1"]).min()
print(nr_1)

countit = otos.count(axis='columns')
print(countit)

countit2 = otos.value_counts()
print(countit2)

#print(groupping)
# res = gb_sales.reset_index()
# res_wide = res.melt(id_vars="Region")
#
# # Setting figure size
# plt.figure(figsize=(10,8))
# # Creating barplot
# sns.barplot(x="Region", y="value",data=res_wide, hue="variable")
# # Show the plot
# plt.show()