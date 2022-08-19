#!/usr/bin/python3
"""Create a random simpson quote Flask API"""

from flask import Flask
import json
import random

app= Flask(__name__)

with open("simpquotes.json") as fileobj:
    simpquotes= json.load(fileobj)

@app.route("/data")
def jsondata():
    # returns all simpson quote data in single page
    return simpquotes

@app.route("/quotes")
def randomquote():

    # randomly choose one of our character dictionaries
    selection= random.choice(simpquotes)

    # get character name and random quote from that dictionary
    randomname= selection["name"]
    randomquote= random.choice(selection["quotes"])
    
    # place those values in a dictionary and return as JSON
    return {"name": randomname, "quote":randomquote}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
    # open local browser and go to 127.0.0.1
