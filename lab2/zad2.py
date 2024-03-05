from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
pca_iris = PCA().fit(X)
cumulative_variance_ratio = np.cumsum(pca_iris.explained_variance_ratio_)   #Pokazuje jaka kolumna ma ile ważnych informacji
# print(cumulative_variance_ratio)

n_components_95 = np.argmax(cumulative_variance_ratio >= 0.95) + 1 #pokazuje od jakiej kolumny zaczyna się 95% ważnych informacji
information_loss = 1 - np.sum(pca_iris.explained_variance_ratio_[:n_components_95]) #pokazuje ile informacji straciliśmy
# print(information_loss)

X_reduced_2d = pca_iris.transform(iris.data)[:, :2]
plt.figure(figsize=(8, 6))
plt.scatter(X_reduced_2d[y == 0, 0], X_reduced_2d[y == 0, 1], label='Setosa', c='red')
plt.scatter(X_reduced_2d[y == 1, 0], X_reduced_2d[y == 1, 1], label='Versicolor', c='blue')
plt.scatter(X_reduced_2d[y == 2, 0], X_reduced_2d[y == 2, 1], label='Virginica', c='green')
plt.legend()
plt.title('PCA 2D dla danych iris')
plt.xlabel('Pierwsza składowa główna PC1')
plt.ylabel('Druga składowa główna PC2')
plt.show()
