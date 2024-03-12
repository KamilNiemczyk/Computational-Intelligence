import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=277982)

X_train, Y_train = train_set[:, 0:4], train_set[:, 4]
X_test, Y_test = test_set[:, 0:4], test_set[:, 4]

tree = DecisionTreeClassifier()  # tworzenie obiektu drzwa

tree_fit = tree.fit(X_train, Y_train)   # trenowanie drzewa

tree_text = export_text(tree_fit, feature_names=df.columns[:4].tolist())  # tworzenie tekstu drzewa

print(tree_text)

predict = tree_fit.predict(X_test)  # przewidywanie klas dla zbioru testowego
print(predict)
poprawne = accuracy_score(Y_test, predict)  # sprawdzanie poprawnosci przewidywan
print(poprawne)

print(confusion_matrix(Y_test, predict))  # macierz bledow
#czyli wychodzi na to, ze zamiast 2 typu raz się pomylił i dał 3 

