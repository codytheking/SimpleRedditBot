#!/usr/bin/env python

import praw
import time
import pathlib
import os.path
import requests

def bot_login():
    r = praw.Reddit('simpleBot',
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
        if "!joke" in comment.body:
            if comment.id not in already_done and comment.author != r.user.me():
                comment_reply = "Here is your requested Chuck Norris joke:\n\n"
                joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']
                comment_reply += ">" + joke
                comment_reply += "\n\nThis joke came from [ICNDB.com](http://icndb.com)"
                
                comment.reply(comment_reply)
                print("posted")
                already_done.append(comment.id)
                
                with open("comments.txt", "a") as f:
                    f.write(comment.id + "\n")

r = bot_login()
already_done = get_saved_comments()
while True:
    run_bot(r, already_done)
    print("Sleep for 10 seconds")
    time.sleep(10)
