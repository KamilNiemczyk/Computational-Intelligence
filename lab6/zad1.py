import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data = pd.read_csv("titanic.csv")
data = data.dropna()
data_encoded = pd.get_dummies(data)
data_encoded = data_encoded.astype(bool).astype(int)
data_encoded = data_encoded.drop(columns=['Unnamed: 0'])
print(data_encoded.head())
frequent_itemsets = apriori(data_encoded, min_support=0.000000001, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.008)

rules_survived = rules[rules['consequents'] == frozenset({'Survived_No'})]

# Sortowanie reguł według ufności
rules_age_adult_sorted = rules_survived.sort_values(by='confidence', ascending=False)


print(rules_age_adult_sorted.head())