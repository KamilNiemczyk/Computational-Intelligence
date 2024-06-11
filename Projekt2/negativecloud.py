import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
from preproces import clubstab

read_from_csv = pd.read_csv("preprocessed.csv")
analyzer = SentimentIntensityAnalyzer()


def get_worst_text_of_every_club():
    worst_text_cloud = ""
    for club in clubstab:
        read_club_column = read_from_csv[club]
        read_club_column = read_club_column.dropna().reset_index(drop=True)
        worst_text = ""
        worst_compound = 1
        for i in range(0, len(read_club_column)):
            sentiment = analyzer.polarity_scores(read_club_column[i])
            if sentiment["compound"] < worst_compound:
                worst_compound = sentiment["compound"]
                worst_text = read_club_column[i]
        worst_text_cloud += worst_text
    return worst_text_cloud

worst_text = get_worst_text_of_every_club()

wordcloud = WordCloud(width = 800, height = 800, background_color='black').generate(worst_text)

wordcloud.to_file("worst_text_cloud.png")

