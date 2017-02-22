#!/usr/bin/env python

import praw
import time
import config
import pathlib
import os.path

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "User-Agent: test bot: 1.0 (by /u/MrKingsBot)")
    return r

def get_saved_comments():
    p = pathlib.Path("comments.txt")
    
    try:
        with p.open() as f:
            coms = f.read();
            coms = coms.split("\n")
            
    except IOError:
        coms = []
    
    return coms
 
def run_bot(r, already_done):
    for comment in r.subreddit('KingsRedditBotTesting').comments(limit=10):
        if "Boogie" in comment.body:
            if comment.id not in already_done and comment.author != r.user.me():
                comment.reply("Run DMC!")
                print("Run DMC!")
                already_done.append(comment.id)
                
                with open("comments.txt", "a") as f:
                    f.write(comment.id + "\n")
    
    print("Sleep for 10 seconds")
    time.sleep(10)

r = bot_login()
already_done = get_saved_comments()
while True:
    run_bot(r, already_done)
    

    
    
    
    
    
    
    
    
    
    
    
    
'''
def run_bot(r):
    #while True:
        for comment in r.subreddit('KingsRedditBotTesting').comments(limit=10):
            if "king" in comment.body:
                print("found!")
                msg = '[me related thread](%s)' % comment.short_link
                r.send_message('_codytheking_', 'Me Thread', msg)
                already_done.append(comment.id)
        #time.sleep(1800)
    
r = bot_login()
run_bot(r)
'''










'''
r = praw.Reddit('PRAW related-question monitor by u/_Daimon_ v 1.0.'
                'Url: https://praw.readthedocs.io/en/latest/'
                'pages/writing_a_bot.html')
r.login()
already_done = []

meWords = ['cody', 'king']
while True:
    subreddit = r.get_subreddit('KingsRedditBotTesting')
    for submission in subreddit.get_hot(limit=10):
        op_text = submission.selftext.lower()
        has_me = any(string in op_text for string in meWords)
        # Test if it contains a me-related question
        if submission.id not in already_done and has_me:
            msg = '[me related thread](%s)' % submission.short_link
            r.send_message('_codytheking_', 'Me Thread', msg)
            already_done.append(submission.id)
    time.sleep(1800)
'''