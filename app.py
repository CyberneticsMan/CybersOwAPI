# importing the requests library
import requests
from flask import Flask

app = Flask(__name__)

# api-endpoint



# sending get request and saving the response as response object


@app.route("/search/<name>")
def search(name):
    URL = f"https://overfast-api.tekrop.fr/players"
    PARAMS = {'name':name}

    r = requests.get(url = URL, params=PARAMS)


    data = r.json()

    return data


@app.route("/search/<name>")
def look(name):
    URL = f"https://overfast-api.tekrop.fr/players/{name}/summary"

    r = requests.get(url = URL)


    data = r.json()

    return data