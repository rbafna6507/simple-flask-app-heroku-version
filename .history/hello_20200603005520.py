from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    import json
    json.dumps('merp merp')
    return 'Hello, World!'