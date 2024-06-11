import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
from preproces import clubstab
from preproces import tokenize
from preproces import remove_stopwords
from preproces import lemmatize
import re

read_from_csv = pd.read_csv("preprocessed.csv")
analyzer = SentimentIntensityAnalyzer()
def remove_emojis(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F" 
                           u"\U0001F300-\U0001F5FF"  
                           u"\U0001F680-\U0001F6FF"  
                           u"\U0001F1E0-\U0001F1FF"  
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"🤣"
                           u"🤭"
                           u"🤔"
                           u"🫠"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def all_oppinion_text_together():
    all_text = ""
    for club in clubstab:
        read_club_column = read_from_csv[club]
        read_club_column = read_club_column.dropna().reset_index(drop=True)
        for i in range(0, len(read_club_column)):
            text_without_emojis = remove_emojis(read_club_column[i])
            all_text += text_without_emojis
    return all_text

def get_worst_words_sentiment():
    word_sentiment = {}
    all_text = all_oppinion_text_together()
    tokenized = tokenize(all_text)
    without_stopwords = remove_stopwords(tokenized)
    lemmatized = lemmatize(without_stopwords)
    for word in lemmatized:
        sentiment = analyzer.polarity_scores(word)
        if word_sentiment.get(word) == None:
            word_sentiment[word] = sentiment["compound"]
    return word_sentiment

worst_words_sentiment = get_worst_words_sentiment()
# worst_words_sentiment = dict(sorted(worst_words_sentiment.items(), key=lambda item: item[1], reverse=True))
best_words_sentiment = dict(sorted(worst_words_sentiment.items(), key=lambda item: item[1], reverse=True))
# print(worst_words_sentiment)
# worst_cloud = WordCloud(width = 800, height = 800, background_color='black').generate_from_frequencies(worst_words_sentiment)
best_cloud = WordCloud(width = 800, height = 800, background_color='black').generate_from_frequencies(best_words_sentiment)
# worst_cloud.to_file("worst_words_cloud.png")
best_cloud.to_file("best_words_cloud.png")