import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=277982)


def classify_iris(sl, sw, pl, pw):
    if sl <= 6 and sw <=5 and pl <= 2:
        return("Setosa")
    elif sl >= 5 and sw > 2.5 and pl > 4.8:
        return("Virginica")
    else:
        return("Versicolor")

good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    sl, sw, pl, pw, species = test_set[i]
    if classify_iris(sl, sw, pl, pw) == species:
        good_predictions = good_predictions + 1

# print(good_predictions)
print(f"Moje dobre odpowiedzi",good_predictions/len*100, "%")

print(train_set)