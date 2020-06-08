from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    json.dumps('Hello, World!')