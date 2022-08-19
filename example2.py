#!/usr/bin/python3
"""Create a random simpson quote Flask API"""

from flask import Flask
from flask import request
import json
import random

app= Flask(__name__)

with open("simpquotes.json") as fileobj:
    simpquotes= json.load(fileobj)

@app.route("/data")
def jsondata():
    """return raw json"""
    return simpquotes

@app.route("/quotes")
def randomquote():

    # attempt to read in any query params "?character=whatever"
    choice= request.args.get("character")

    # EITHER a character was provided OR the character query param wasn't used
    # check if there was one!
    if choice:
        # write code that pulls that character from simpquotes
        # choice = "Lisa"
        # loop over simpquotes and find characters that match that name
        for simpdict in simpquotes:
            if choice in simpdict["name"]:
                # after the first match
                selection= simpdict
                break

    else:
        # randomly choose one of our character dictionaries
        selection= random.choice(simpquotes)

    randomname= selection["name"]
    randomquote= random.choice(selection["quotes"])
    return {"name": randomname, "quote":randomquote}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    # open local browser and go to 127.0.0.1
