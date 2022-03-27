from datetime import datetime
from flask import Flask
from suds.client import Client

app = Flask("__name__")
client = Client('http://bb1d-193-40-13-171.ngrok.io/', cache=None)

@app.route('/')
def index():
    return client.service.your_method_name(arguments)


if __name__ == "__main__":
    app.run(debug=True)
