# affinity propagation clustering
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

my_correlation = pd.read_csv("data/cluster_source_202202.csv", sep=",", usecols=["local_cc_10", "edges_10"])
print(my_correlation)

# define dataset
kmeans = KMeans(n_clusters=4).fit(my_correlation)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(my_correlation['local_cc_10'], my_correlation['edges_10'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()