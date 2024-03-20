import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=277982)

# print("Etykiety klas dla zbioru treningowego:")
# print(set(train_set[:, -1]))

clf = MLPClassifier(hidden_layer_sizes=(2,), max_iter=3000, random_state=277982)
clf.fit(train_set[:, 0:4], train_set[:, 4])
ratio1 = clf.score(test_set[:, 0:4], test_set[:, 4])
print(f"Poprawne odpowiedzi 2 neurony: {ratio1*100}%")

clf_3_neurons = MLPClassifier(hidden_layer_sizes=(3,), max_iter=3000, random_state=277982)
clf_3_neurons.fit(train_set[:, 0:4], train_set[:, 4])
ratio2 = clf_3_neurons.score(test_set[:, 0:4], test_set[:, 4])
print(f"Poprawne odpowiedzi 3 neurony: {ratio2*100}%")

clf_3_3_neurons = MLPClassifier(hidden_layer_sizes=(3, 3), max_iter=3000, random_state=277982)
clf_3_3_neurons.fit(train_set[:, 0:4], train_set[:, 4])
ratio3 = clf_3_3_neurons.score(test_set[:, 0:4], test_set[:, 4])
print(f"Poprawne odpowiedzi 2 warstwy po 3 neurony: {ratio3*100}%")

