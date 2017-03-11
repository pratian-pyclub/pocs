import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns; sns.set() # for plot styling

from sklearn.datasets import load_digits
from sklearn.cluster import KMeans

from scipy.stats import mode
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.manifold import TSNE

digits = load_digits()
digits.data.shape

tsne = TSNE(n_components=2, init='random', random_state=0)
digits_proj = tsne.fit_transform(digits.data)

kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(digits_proj)

# (10, 2)
# 0.919309961046

print kmeans.cluster_centers_.shape

labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(digits.target[mask])[0]

print accuracy_score(digits.target, labels)

mat = confusion_matrix(digits.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=digits.target_names,
            yticklabels=digits.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');

plt.show()
