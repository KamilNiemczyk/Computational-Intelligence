import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler, StandardScaler


iris = datasets.load_iris()
X = iris.data
y = iris.target

iris_df = pd.DataFrame(X, columns=iris.feature_names)
iris_df['Species'] = y
species_names = iris.target_names

# Wybór dwóch zmiennych: sepal length i sepal width
X_sepal = iris.data[:, :2]

# Tworzenie wykresu dla danych oryginalnych
plt.figure(figsize=(10, 5))
sns.scatterplot(x=X_sepal[:, 0], y=X_sepal[:, 1], hue=species_names[y])
plt.title('Dane oryginalne')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(title='Species')
plt.grid(True)
plt.show()

#Z-score czyli odchylenie wartości od średniej
scaler_zscore = StandardScaler()
X_sepal_zscore = scaler_zscore.fit_transform(X_sepal)

# Wykres dla danych zeskalowanych z-scorem
plt.figure(figsize=(10, 5))
sns.scatterplot(x=X_sepal_zscore[:, 0], y=X_sepal_zscore[:, 1], hue=species_names[y])
plt.title('Dane zeskalowane z-scorem')
plt.xlabel('Sepal Length (zeskalowane)')
plt.ylabel('Sepal Width (zeskalowane)')
plt.legend(title='Species')
plt.grid(True)
plt.show()

#Normalizacja min-max czyli przeskalowanie wartości do przedziału [0, 1] proporcjonalnie
scaler_minmax = MinMaxScaler()
X_sepal_minmax = scaler_minmax.fit_transform(X_sepal)

# Wykres dla danych znormalizowanych min-max 
plt.figure(figsize=(10, 5))
sns.scatterplot(x=X_sepal_minmax[:, 0], y=X_sepal_minmax[:, 1], hue=species_names[y])
plt.title('Dane znormalizowane min-max')
plt.xlabel('Sepal Length (znormalizowane)')
plt.ylabel('Sepal Width (znormalizowane)')
plt.legend(title='Species')
plt.grid(True)
plt.show()

