from flask import Flask
import requests

app = Flask(__name__)

@app.route("/hundredPosts")
def hello_world():
    x=requests.get('https://jsonplaceholder.typicode.com/posts')
    return x.text