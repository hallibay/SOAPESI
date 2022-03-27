from datetime import datetime
from flask import Flask
from suds.client import Client

app = Flask("__name__")
client = Client('https://bb1d-193-40-13-171.ngrok.io/?wsdl', cache=None)

@app.route('/')
def index():
    return "hello world"



if __name__ == "__main__":
    app.run(debug=True)
