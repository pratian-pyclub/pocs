from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# Loading the basic iris dataset
iris = datasets.load_iris()

# PCA uses dimensionality reduction to find the highly covarient dimension(features)
# We are reducing down to one dimension to see the graph 
n_components = 2

# Splitting the dataset
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.0, random_state=1)
pca = PCA(n_components = n_components)
pca.fit(iris.data)

x_train_pca = pca.transform(x_train)
X = x_train_pca.T[0]
Y = x_train_pca.T[1]

# In our case, 4 features are reduced to 2 features.
# In images, the pixels will be of 4096 etc.
# Those are features. And they can be reduced from few thousands to few hundreds
for x,y,z in zip(X,Y,y_train):
	if z==0:
		plt.plot(x,y,'ro')
	elif z==1:
		plt.plot(x,y,'bo')
	else:
		plt.plot(x,y,'go')
		
# Displaying the plotted image
plt.show()
