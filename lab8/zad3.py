import praw
import pandas as pd
# Read-only instance
reddit_read_only = praw.Reddit(client_id="rO84FKV0Zt0TTF2sasoJdQ",         # your client id
                               client_secret="AMN8cOPc-FPx-f8Zf40znZpmk0hRNg",      # your client secret
                               user_agent="Kamil")        # your user agent
 

def write_post_to_file(post):
    with open('posts.txt', 'ab') as file:
        file.write("Title: ".encode('utf-8'))
        file.write((post.title + '\n').encode('utf-8'))
        file.write((post.selftext + '\n').encode('utf-8'))
        file.write("____________________________________________________________".encode('utf-8'))
        file.write(('\n'.encode('utf-8')))


subreddit = reddit_read_only.subreddit('PremierLeague')

for post in subreddit.search(limit=100):
    write_post_to_file(post)


