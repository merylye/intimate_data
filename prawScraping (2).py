import praw
import datetime

reddit = praw.Reddit(
    client_id = "AIc6MLL_haY5bQ",
    client_secret="NrbXqneVU66m45DJQ1ZSXXHOcct5pg",
    user_agent="web:designing.ai.group:v1 (by u/intimatedata)",
    username="intimatedata",
    password="qwerty123!",
)

print(reddit.read_only)

subreddit = reddit.subreddit("BabyBumps")

print(subreddit.display_name)

import pandas as pd

submissions = []
for submission in subreddit.hot(limit=100):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        top_comment = top_level_comment.body
        if len(top_comment) > 400:
            submissions.append([submission.subreddit, submission.url, datetime.datetime.fromtimestamp(submission.created), submission.title,
            submission.selftext, top_comment])
submissions = pd.DataFrame(submissions,columns=['subreddit', 'url', 'date_created', 'title', 'body', 'top_comment'])

submissions.to_csv(r'C:\Users\meryl\OneDrive\Desktop\NewBabyBumps.csv', index = False, header=True)
print(submissions)
