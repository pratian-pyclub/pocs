import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns; sns.set() # for plot styling

from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

path = "/Users/swaathi/Skcript/Pratian/pocs/scikit-scripts/leaves-train.csv"

df = pd.read_csv(path, index_col='id')
df.drop(['species'], axis=1, inplace=True)

kmeans = KMeans(n_clusters=99, random_state=0)
clusters = kmeans.fit_predict(df)

kmeans.cluster_centers_.shape
# (99, 192)
clusters.shape
# (990,)

centers = kmeans.cluster_centers_.reshape(99, 3, 64)
fig, ax = plt.subplots(9, 11, figsize=(3,3))

# ==================================================

val = """0.007812,0.023438,0.023438,0.003906,0.011719,0.009766,0.027344,0,0.001953,0.033203,0.013672,0.019531,0.066406,0,0.029297,0,0.03125,0.011719,
0,0.025391,0.023438,0.001953,0,0.015625,0,0.03125,0,0.013672,0.029297,0.015625,0.011719,0.003906,0.025391,0,0.001953,0.011719,0.009766,0.041016,0.037109,
0.019531,0,0.009766,0.021484,0.015625,0.007812,0.013672,0.027344,0.0625,0,0.017578,0.03125,0,0.044922,0.007812,0.025391,0.003906,0.013672,0.015625,
0.013672,0.003906,0.005859,0.003906,0.019531,0.001953,0.00064671,0.00060945,0.0005765,0.0005534,0.00051575,0.00049629,0.00047438,0.00045284,0.00045398,
0.00042897,0.00041751,0.00040968,0.00040551,0.00039822,0.00039905,0.00038939,0.00039857,0.00041616,0.00041438,0.00043008,0.00042179,0.00043667,
0.00045212,0.00046713,0.00047021,0.00048446,0.0004891,0.00048976,0.00047542,0.00048608,0.00048383,0.00049999,0.00051287,0.00051148,0.00051886,0.00051302,
0.0005016,0.00049765,0.00048718,0.0004707,0.00045796,0.00043969,0.00043607,0.0004267,0.00039426,0.00038507,0.00038236,0.00036998,0.00036658,0.0003726,
0.00038577,0.00038888,0.00039102,0.00041379,0.00042159,0.00043435,0.00045229,0.00047083,0.00048544,0.00051234,0.00053558,0.00055327,0.00060969,
0.0006605,0.049805,0.017578,0.003906,0.024414,0.001953,0.010742,0.035156,0.007812,0.039062,0.0625,0,0,0.007812,0.007812,0,0,0.047852,0,0.054688,0.022461,
0,0.000977,0.018555,0.001953,0.008789,0.015625,0.044922,0,0.037109,0.012695,0.02832,0,0.019531,0.026367,0.005859,0,0.004883,0.016602,0.03418,
0.056641,0.006836,0.000977,0.022461,0.037109,0.004883,0.021484,0.035156,0.000977,0.004883,0.015625,0,0,0.006836,0.037109,0.007812,0,0.00293,0.00293,
0.035156,0,0,0.004883,0,0.025391"""

val = """0.005859,0.009766,0.019531,0.007812,0.003906,0.005859,0.068359,0,0,0.044922,0.007812,0.011719,0.021484,0.001953,0.025391,0,0.009766,0.011719,
0.007812,0.005859,0.041016,0.001953,0,0.015625,0,0.009766,0.001953,0.009766,0.009766,0.015625,0.005859,0,0.017578,0.007812,0.005859,0.009766,0.019531,
0.042969,0.021484,0.001953,0,0.005859,0.015625,0.009766,0.011719,0.011719,0.03125,0.10938,0,0.046875,0.03125,0,0.035156,0,0.10547,0,0.015625,0.015625,
0.019531,0.001953,0,0.005859,0.011719,0.007812,0.00097311,0.00091025,0.00087015,0.00082612,0.00079573,0.00076342,0.00072933,0.00070181,0.00066375,
0.00062857,0.00059769,0.00056993,0.00054563,0.0005262,0.00050005,0.00049443,0.00048438,0.0004902,0.00049106,0.00050741,0.00052463,0.00056266,0.00060433,
0.00066326,0.00070833,0.00076308,0.00082441,0.00088587,0.00095649,0.0010303,0.0011021,0.0011779,0.0011926,0.0011178,0.0010486,0.00098242,0.00091935,
0.0008624,0.00080939,0.00076113,0.00070237,0.00065397,0.00061421,0.0005739,0.00054917,0.00052426,0.00051092,0.00049375,0.00049475,0.00049702,0.00051032,
0.00053295,0.00055168,0.00058667,0.00061046,0.00063864,0.00066957,0.00069733,0.00073939,0.00078929,0.00083566,0.0008824,0.00091113,0.00097073,0.003906,
0.047852,0.008789,0,0.097656,0.005859,0.003906,0.10156,0.032227,0,0,0.066406,0.007812,0.006836,0,0,0.057617,0,0,0.027344,0,0,0.070312,0,0.000977,0,0.000977,
0.003906,0.035156,0.015625,0.027344,0,0,0.008789,0.015625,0,0,0.011719,0.000977,0.000977,0,0,0,0.005859,0.022461,0.020508,0.021484,0.056641,0.010742,0.008789,
0,0,0.000977,0,0.1543,0,0.005859,0.000977,0.007812,0,0,0,0.020508,0.00293
"""

x = np.array(val.split(",")).astype(float).reshape(3,64)
margin = x[0].reshape(8,8)
shape = x[1].reshape(8,8)
texture = x[1].reshape(8,8)

# ==================================================

from __future__ import print_function

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

print(__doc__)

# Generating the sample data from make_blobs
# This particular setting has one distinct cluster and 3 clusters placed close
# together.
X, y = make_blobs(n_samples=500,
                  n_features=2,
                  centers=4,
                  cluster_std=1,
                  center_box=(-10.0, 10.0),
                  shuffle=True,
                  random_state=1)  # For reproducibility

range_n_clusters = [2, 3, 4, 5, 6]

for n_clusters in range_n_clusters:
    # Create a subplot with 1 row and 2 columns
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)

    # The 1st subplot is the silhouette plot
    # The silhouette coefficient can range from -1, 1 but in this example all
    # lie within [-0.1, 1]
    ax1.set_xlim([-0.1, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, random_state=10)
    cluster_labels = clusterer.fit_predict(X)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(X, cluster_labels)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.spectral(float(i) / n_clusters)
        ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    ax1.set_title("The silhouette plot for the various clusters.")
    ax1.set_xlabel("The silhouette coefficient values")
    ax1.set_ylabel("Cluster label")

    # The vertical line for average silhouette score of all the values
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

    ax1.set_yticks([])  # Clear the yaxis labels / ticks
    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    # 2nd Plot showing the actual clusters formed
    colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
    ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                c=colors)

    # Labeling the clusters
    centers = clusterer.cluster_centers_
    # Draw white circles at cluster centers
    ax2.scatter(centers[:, 0], centers[:, 1],
                marker='o', c="white", alpha=1, s=200)

    for i, c in enumerate(centers):
        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50)

    ax2.set_title("The visualization of the clustered data.")
    ax2.set_xlabel("Feature space for the 1st feature")
    ax2.set_ylabel("Feature space for the 2nd feature")

    plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                  "with n_clusters = %d" % n_clusters),
                 fontsize=14, fontweight='bold')

    plt.show()

# ==================================================

from sklearn.datasets import load_digits
digits = load_digits()
digits.data.shape

kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(digits.data)
kmeans.cluster_centers_.shape

from scipy.stats import mode

labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(digits.target[mask])[0]

from sklearn.metrics import accuracy_score
accuracy_score(digits.target, labels)
