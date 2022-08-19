import requests
import json
from pprint import pprint

character= "Homer Simpson"
quote= "That dog has a puffy tail!!!"

# try running this script with a new character!
#character= "Mr. Burns"
#quote= "Seeeeeee myyyyyy vest! See my vest! Made from real gorilla chest!"

# put variables into a dictionary
newchar= {"name": character, "quote": quote}

# convert python dict into json string
newcharjson= json.dumps(newchar)

# sending a post request to /new with JSON data attached!
resp= requests.post("http://127.0.0.1:2224/new", json=newcharjson)

# display changed data!
pprint(resp.json())
