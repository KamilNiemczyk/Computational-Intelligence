from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter

def tokenize(text):
    return word_tokenize(text)

def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def count_words(text):
    return len(text)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    return [word for word in text if word.lower() not in stop_words]

def remove_stopwords_additional(text):
    stop_words = set(stopwords.words('english'))
    additional_stopwords = ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '"', "'"]
    stop_words.update(additional_stopwords)
    return [word for word in text if word.lower() not in stop_words]

def lemmatize(text):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in text]

def diff_between_two_texts(text1, text2):
    tab = []
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            tab.append((text1[i], text2[i]))
    return tab

def most_10_common_words(text):
    counter = Counter(text)
    most_10_common_words = counter.most_common(10)
    words, counts = zip(*most_10_common_words)
    return words, counts

def main():
    text = read_file('text.txt')
    tokenized_text = tokenize(text)
    without_stopwords = remove_stopwords(tokenized_text)
    without_stopwords_additional = remove_stopwords_additional(tokenized_text)
    lemmatized_text = lemmatize(without_stopwords_additional)
    # dif = diff_between_two_texts(without_stopwords_additional, lemmatized_text)
    print("Words after tokenize: " + str(count_words(tokenized_text)))
    print("Words after removing stopwords: " + str(count_words(without_stopwords)))
    print("Words after removing stopwords and additional stopwords: " + str(count_words(without_stopwords_additional)))
    print("Words after lemmatization: " + str(count_words(lemmatized_text)))
    words, counts = most_10_common_words(lemmatized_text)
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.title('Most common words')
    plt.show()






main()