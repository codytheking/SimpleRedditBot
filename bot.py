#!/usr/bin/env python

import praw
import time
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "MrKingsBot comment searcher v1.0")
    return r
    

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