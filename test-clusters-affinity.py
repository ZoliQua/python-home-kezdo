# Python Test Project File
# Written by Zoltan Dul (2021)
#
# affinity propagation clustering
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot
import pandas as pd

my_correlation = pd.read_csv("data/cluster_source_202202.csv", sep=",", usecols=["GO_ID", "SPECIES", "local_cc_10", "edges_10"])
print(my_correlation)

# define dataset
X, _ = make_classification(n_samples=1000, n_features=4, n_informative=4, n_redundant=0, n_clusters_per_class=1, random_state=4)
# define the model
model = AffinityPropagation(damping=0.9)
# fit the model
model.fit(X)
# assign a cluster to each example
yhat = model.predict(X)
# retrieve unique clusters
clusters = unique(yhat)
# create scatter plot for samples from each cluster
for cluster in clusters:
	# get row indexes for samples with this cluster
	row_ix = where(yhat == cluster)
	# create scatter of these samples
	pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# show the plot
pyplot.show()
print(X[0][0])