import pandas as pd
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        list = data.split("Comment:")
    return list

def tokenize(text):
    return word_tokenize(text)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    additional_stopwords = ['.', ',', '!', '?', '(', ')', '[', ']', '{', '}', ':', ';', '\'', '\"', '``', '...', '’', '“', '”', '–', '—', '‘',"''", '``', "\n"]
    stop_words.update(additional_stopwords)
    return [word for word in text if word.lower() not in stop_words]

def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in text]

a = read_file("./posts/arsenal.txt")
# text = a[12]
# tokenized = tokenize(text)
# without_stopwords = remove_stopwords(tokenized)
# lemmatized = lemmatize(without_stopwords)
# together = ' '.join(lemmatized)
# print(together)
def preprocess_text(text):
    tokenized = tokenize(text)
    without_stopwords = remove_stopwords(tokenized)
    lemmatized = lemmatize(without_stopwords)
    together = ' '.join(lemmatized)
    return together
clubstab = ["arsenal", "aston_villa", "bournemouth", "brentford", "brighton", "burnley", "chelsea", "crystal_palace", "everton", "fulham", "liverpool", "luton", "manchester_city", "manchester_united", "newcastle", "nottingham", "sheffield", "tottenham", "west_ham", "wolverhampton"]
df = pd.DataFrame()
for club in clubstab:
    a = read_file("./posts/" + club + ".txt")
    for i in range(0, len(a)):
        a[i] = preprocess_text(a[i])
    df[club] = pd.Series(a)
df.to_csv("preprocessed.csv")