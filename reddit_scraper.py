#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

# Reddit API credentials set up
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

# Which subreddit will it be scraping?
subreddit = reddit.subreddit('Python')

# How many subreddit threads to scrape?
top_subreddit = subreddit.top(limit=10)

# Print out titles of threads
for submission in subreddit.top(limit=10):
    print(submission.title, submission.id)

# Set up dict for some data fields
topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "comms_num": [],
                "created": [],
                "body":[]}

# Put stuff into the dict
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

# Pop it in a dataframe
topics_data = pd.DataFrame(topics_dict)

# Patch through to your eyes
print(topics_data)
