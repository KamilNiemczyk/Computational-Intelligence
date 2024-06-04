from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

analyzer = SentimentIntensityAnalyzer()

first_oppinion = "We stayed at the apt 3. The property is a bit run down. The mattress in our room had one side that was sunken in so badly that I kept sliding off it. The entrance to the apartment was not clean and could use a bit of renovation (as in, plaster and paint).The pillows in our room could also be replaced, as they were extremely lumpy."
second_oppinion = "I loved the vibe it was sooo funnnn and loverly I shared a room with three of the kkiindeeessstt Argentinian young ladies. I am a wheelchair user sooooo I think the young lady at reception picked it especially for me. I had the best night sleep. Thank you so much for making it an absolute best delight to stay and breakfast was fffanntttasstiic tooooo I had a brilliant young member of staff who filled up my plates with the full English breakfast and buffet and nothing was too much trouble..."

negative = analyzer.polarity_scores(first_oppinion)
positive = analyzer.polarity_scores(second_oppinion)

nlp = pipeline("sentiment-analysis")
negative_text = nlp(first_oppinion)[0]
positive_text = nlp(second_oppinion)[0]


print("First oppinion: ", negative)
print("Second oppinion: ", positive)

print("First oppinion: ", negative_text)
print("Second oppinion: ", positive_text)

# First oppinion:  {'neg': 0.089, 'neu': 0.911, 'pos': 0.0, 'compound': -0.7391}
# Second oppinion:  {'neg': 0.024, 'neu': 0.721, 'pos': 0.255, 'compound': 0.9799}
# First oppinion:  {'label': 'NEGATIVE', 'score': 0.999797523021698}
# Second oppinion:  {'label': 'POSITIVE', 'score': 0.9978544116020203}