#!/usr/bin/env python

import praw
import time
import config
import re

def bot_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "User-Agent: test bot: 1.0 (by /u/MrKingsBot)")
    return r

def run_bot(r):
    already_done = []
    while True:
        for comment in r.subreddit('microsoft').comments(limit=10):
            if "Linux" or "linux" in comment.body:
                if comment.id not in already_done:
                    #comment.reply("Oh boy")
                    print(comment.body)
                    #msg = '[me related thread](%s)' % comment.short_link
                    #r.send_message('_codytheking_', 'Me Thread', msg)
                    already_done.append(comment.id)
        time.sleep(60)

r = bot_login()
run_bot(r)











'''
r = praw.Reddit('PRAW testing by u/_MrKingsBot_ v 1.0.')
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
