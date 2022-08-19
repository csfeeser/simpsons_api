#!/usr/bin/python3
"""Create a random simpson quote Flask API"""

from flask import Flask
from flask import request
from flask import redirect
import json
import random

app= Flask(__name__)

with open("files/simpquotes.json") as fileobj:
    simpquotes= json.load(fileobj)

@app.route("/new", methods= ["POST"]) 
def getquotes():
    # add new quotes/characters
    # POST JSON data that is added to simpquotes
    
    # any json data attached to a request
    # will be put in the object "datatouse"
    datatouse= request.json
    
    # convert incoming json into python
    datatouse= json.loads(datatouse)
    
    # holding the new data as variables
    newname= datatouse["name"]
    newquote= datatouse["quote"]

    # newname= "Homer Simpson"
    # newquote= "That dog has a puffy tail!"

    # check if character already in simpquotes
    present= False
    for x in simpquotes:
        if newname == x["name"]:
            present= True
            # add new quote to existing character
            x["quotes"].append(newquote)
         
    # if it's a new character:
    if not present:
        simpquotes.append({"name": newname,
                           "quotes": [newquote]})

    # YOU ALWAYS NEED TO SEND A RESPONSE BACK
    return redirect("/data") 


@app.route("/data") # DEFAULT GET
def jsondata():
    """return raw json"""
    return simpquotes

@app.route("/quotes", methods=["GET"])
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
