import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix


df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=277982)

X_train, Y_train = train_set[:, 0:4], train_set[:, 4]
X_test, Y_test = test_set[:, 0:4], test_set[:, 4]

#k-NN, k=3
neighbours = KNeighborsClassifier(n_neighbors=3)
neighbours_fit = neighbours.fit(X_train, Y_train)
predict = neighbours_fit.predict(X_test)
poprawne = accuracy_score(Y_test, predict)
print("k-NN, k=3")
print(poprawne)
# print(confusion_matrix(Y_test, predict))

#k-NN, k=5
neighbours = KNeighborsClassifier(n_neighbors=5)
neighbours_fit = neighbours.fit(X_train, Y_train)
predict = neighbours_fit.predict(X_test)
poprawne = accuracy_score(Y_test, predict)
print("k-NN, k=5")
print(poprawne)
# print(confusion_matrix(Y_test, predict))

#k-NN, k=11
neighbours = KNeighborsClassifier(n_neighbors=11)
neighbours_fit = neighbours.fit(X_train, Y_train)
predict = neighbours_fit.predict(X_test)
poprawne = accuracy_score(Y_test, predict)
print("k-NN, k=11")
print(poprawne)
# print(confusion_matrix(Y_test, predict))

#Naive Bayes
gnb = GaussianNB()
gnb_fit = gnb.fit(X_train, Y_train)
predict = gnb_fit.predict(X_test)
poprawne = accuracy_score(Y_test, predict)
print("Naive Bayes")
print(poprawne)
# print(confusion_matrix(Y_test, predict))
