import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
read_from_csv = pd.read_csv("preprocessed.csv")
read_arsenal_column = read_from_csv["arsenal"]
read_arsenal_column = read_arsenal_column.dropna().reset_index(drop=True)
import matplotlib.pyplot as plt
# read_first_row = read_arsenal_column[13]
analyzer = SentimentIntensityAnalyzer()


from preproces import clubstab

all_compounds_dict = {}

def get_compound_score(club):
    read_club_column = read_from_csv[club]
    read_club_column = read_club_column.dropna().reset_index(drop=True)
    for i in range(0, len(read_club_column)):
        sentiment = analyzer.polarity_scores(read_club_column[i])
        if all_compounds_dict.get(club) == None:
            all_compounds_dict[club] = [sentiment["compound"]]
        else:
            all_compounds_dict[club].append(sentiment["compound"])

def calculate_clubs_compound():
    for club in clubstab:
        get_compound_score(club)

def get_avarage_compound(dict):
    for key in dict:
        sum = 0
        for i in range(0, len(dict[key])):
            sum += dict[key][i]
        dict[key] = sum / len(dict[key])
    return dict

def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))



calculate_clubs_compound()
clubs_avarage_compound = get_avarage_compound(all_compounds_dict)
sorted_clubs_by_avarage = sort_dict(clubs_avarage_compound)
print(sorted_clubs_by_avarage)

clubs = list(sorted_clubs_by_avarage.keys())
compound = list(sorted_clubs_by_avarage.values())
club_color = {
    "arsenal": "red",
    "aston_villa": "brown",
    "bournemouth": "red",
    "brentford": "red",
    "brighton": "blue",
    "burnley": "lightblue",
    "chelsea": "blue",
    "crystal_palace": "blue",
    "everton": "blue",
    "fulham": "black",
    "liverpool": "red",
    "luton": "orange",
    "manchester_city": "lightblue",
    "manchester_united": "red",
    "newcastle": "black",
    "nottingham": "red",
    "sheffield": "red",
    "tottenham": "black",
    "west_ham": "brown",
    "wolverhampton": "yellow"
}
plt.figure(figsize=(20, 10))

plt.bar(clubs, compound, color=[club_color[club] for club in clubs])
plt.xticks(rotation=90)
plt.xlabel('Clubs')
plt.ylabel('Compound')
plt.title('Clubs and their compound scores')

plt.savefig("compound_scores.png")

