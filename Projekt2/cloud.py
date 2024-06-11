import pandas as pd
import matplotlib.pyplot as plt
from preproces import clubstab
from wordcloud import WordCloud

read_from_csv = pd.read_csv("preprocessed.csv")

def get_text_from_all_clubs():
    all_clubs_text = ""
    for club in clubstab:
        read_club_column = read_from_csv[club]
        read_club_column = read_club_column.dropna().reset_index(drop=True)
        for i in range(0, len(read_club_column)):
            all_clubs_text += read_club_column[i]
    return all_clubs_text

wordcloud = WordCloud(width = 800, height = 800, background_color='black').generate(get_text_from_all_clubs())

# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

wordcloud.to_file("wordcloud.png")

    



