# synthetic classification dataset
from numpy import where
from sklearn.datasets import make_classification


import pandas as pd
go_data = pd.read_csv("data/cluster_source_202202_mod_extract.csv", sep=",", usecols=["GO_ID", "SPECIES", "local_cc_10", "edges_10"])
#print(my_correlation)


# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(color_codes=True)
iris = sns.load_dataset("iris")
flights = sns.load_dataset("flights")
species = iris.pop("species")

flights = flights.pivot("month", "year", "passengers")
#print(flights)

go_data2 = go_data[(go_data.SPECIES == "SP") | (go_data.SPECIES == "SC") | (go_data.SPECIES == "AT") | (go_data.SPECIES == "HS") | (go_data.SPECIES == "DM") | (go_data.SPECIES == "DR") | (go_data.SPECIES == "CE")]
print(go_data2)

go_data_pivot = go_data2.pivot("GO_ID", "SPECIES", "edges_10")
#print(my_correlation)

g = sns.clustermap(go_data_pivot, figsize=(10, 10), annot=True, cmap="YlGnBu", mask=(go_data_pivot==0), standard_scale=1)
# row_cluster=False,
print(dir(g))
#display(g.data())
print(g.data2d.T)
g.data2d.T.to_excel("edges_10_annotation_normal_scale_20220901b.xlsx")

plt.show()
