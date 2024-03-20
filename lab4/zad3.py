import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("diabetes.csv")

X = df.values[:, 0:8]
Y = df.values[:, 8]

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=277982)

clf = MLPClassifier(hidden_layer_sizes=(6,3), activation='relu', max_iter=500)

clf.fit(train_set[:, 0:8], train_set[:, 8])

ratio1 = clf.score(test_set[:, 0:8], test_set[:, 8])
print(f"Poprawne odpowiedzi 6,3 neurony: {ratio1*100}%")

macierz = confusion_matrix(test_set[:, 8], clf.predict(test_set[:, 0:8]))
print(macierz)
#gorsze są błedy FN, bo wtedy nie wykryje choroby
