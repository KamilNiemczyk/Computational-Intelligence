import pandas as pd

#zad1a
df = pd.read_csv("iris_with_errors.csv")
brakujace = df.isnull().sum().sum()
# print(brakujace)
# print(df.describe())

# zad1b
for column in df.columns:
    if column != 'variety':
        df[column] = pd.to_numeric(df[column], errors='coerce')     #zmiana typu kolumn na numeryczne
# for column in df.columns:
#     print(column, df[column].dtype)         #sprawdzenie typów kolumn

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
for column in numeric_columns:             #wypełnienie brakujących wartości średnią z kolumny
    df[column] = df[column].apply(lambda x: x if 0 < x < 15 else df[column].mean())

#zad1c
def zastąp(x):
    lista  = ['setosa', 'versicolor', 'virginica']
    mala = x.lower()
    tempslowo = ""
    licznik = 0            
    def ilerazyliterawslowie(litera, slowo):
        licznik = 0
        for liter in slowo:
            if liter == litera:
                licznik += 1
        return licznik
    for slowo in lista:
        nowylicznik = 0
        for litera in slowo:
            nowylicznik = ilerazyliterawslowie(litera, mala) + nowylicznik
        if nowylicznik > licznik:
            licznik = nowylicznik
            tempslowo = slowo
    return tempslowo.capitalize()

df['variety'] = df['variety'].apply(lambda x: x if x in ['Setosa', 'Versicolor', 'Virginica'] else zastąp(x))
# print(df['variety'].value_counts())



