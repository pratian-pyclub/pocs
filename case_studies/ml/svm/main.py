from sklearn import datasets
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import decomposition
from sklearn.metrics import confusion_matrix

# Setting to print the confusion matrix in singleline
np.set_printoptions(threshold=np.nan, linewidth=180)

# This dataset has 400 face images of 40 persons i.e, 10 images per person.
# This is a 64*64 pixel image

faces = datasets.fetch_olivetti_faces()
data = faces.data
labels = faces.target

n_images = data.shape[0]
n_features = data.shape[1]
n_components = 85
n_classes = 40

# Splitting the training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.25, random_state=42)


# Using PCA to feature extract. Dropping the number of dimensions to
# n_components
pca = decomposition.PCA(n_components=n_components)
# Fitting the PCA with whole face data
pca.fit(data)

# Dimensionality Reduction on training and testing datas
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# SVM Classifier to predict the faces with the reduced dimensions from PCA
# output
clf = SVC(kernel='rbf', class_weight='balanced')
# Fitting with X and Y values
clf = clf.fit(X_train_pca, y_train)
# Calling predict method on classifier for test data
y_pred = clf.predict(X_test_pca)

# Building the confusion matrix to see where the errors happened
x = confusion_matrix(y_test, y_pred, labels=range(n_classes))

# Calculating accuracy at last
accuracy = np.sum(np.diag(x)) * 100 / np.sum(x)
print x
print 'Accuarcy is : ', accuracy
