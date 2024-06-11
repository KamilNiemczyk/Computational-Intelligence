import praw
import pandas as pd
from tqdm import tqdm
import time 
# Read-only instance
reddit_read_only = praw.Reddit(client_id="*******",         
                               client_secret="*******",      
                               user_agent="*******",
                                username="*********",
                                password="*********")
 

def write_post_to_file(post, filename):
    with open(filename, 'ab') as file:
        post.comments.replace_more(limit=None)
        top_comments = sorted(post.comments, key=lambda comment: comment.score, reverse=True)[:20]
        for comment in top_comments:
            file.write("Comment: ".encode('utf-8'))
            file.write((comment.body + '\n').encode('utf-8')) 
        file.write(('\n'.encode('utf-8')))


subreddit = reddit_read_only.subreddit('PremierLeague')

for post in tqdm(subreddit.search('Arsenal', limit=25), desc='Downloading posts about Arsenal'):
    write_post_to_file(post, "arsenal.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Fulham', limit=25), desc='Downloading posts about Fulham'):
    write_post_to_file(post, "fulham.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Liverpool', limit=25), desc='Downloading posts about Liverpool'):
    write_post_to_file(post, "liverpool.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Manchester United', limit=25), desc='Downloading posts about Manchester United'):
    write_post_to_file(post, "manchester_united.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Manchester City', limit=25), desc='Downloading posts about Manchester City'):
    write_post_to_file(post, "manchester_city.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Chelsea', limit=25), desc='Downloading posts about Chelsea'):
    write_post_to_file(post, "chelsea.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Tottenham Hotspur', limit=25), desc='Downloading posts about Tottenham'):
    write_post_to_file(post, "tottenham.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Brentford', limit=25), desc='Downloading posts about Brentford'):
    write_post_to_file(post, "brentford.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('West Ham United', limit=25), desc='Downloading posts about West Ham United'):
    write_post_to_file(post, "west_ham.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Newcastle United', limit=25), desc='Downloading posts about Newcastle United'):
    write_post_to_file(post, "newcastle.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Crystal Palace', limit=25), desc='Downloading posts about Crystal Palace'):
    write_post_to_file(post, "crystal_palace.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Aston Villa', limit=25), desc='Downloading posts about Aston Villa'):
    write_post_to_file(post, "aston_villa.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Everton', limit=25), desc='Downloading posts about Everton'):
    write_post_to_file(post, "everton.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Bournemouth', limit=25), desc='Downloading posts about Bournemouth'):
    write_post_to_file(post, "bournemouth.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Brighton & Hove Albion', limit=25), desc='Downloading posts about Brighton & Hove Albion'):
    write_post_to_file(post, "brighton.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Burnley', limit=25), desc='Downloading posts about Burnley'):
    write_post_to_file(post, "burnley.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Luton Town', limit=25), desc='Downloading posts about Luton Town'):
    write_post_to_file(post, "luton.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Nottingham Forest', limit=25), desc='Downloading posts about Nottingham Forest'):
    write_post_to_file(post, "nottingham.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Wolverhampton Wanderers', limit=25), desc='Downloading posts about Wolverhampton Wanderers'):
    write_post_to_file(post, "wolverhampton.txt")
    time.sleep(1)

for post in tqdm(subreddit.search('Sheffield United', limit=25), desc='Downloading posts about Sheffield United'):
    write_post_to_file(post, "sheffield.txt")
    time.sleep(1)





