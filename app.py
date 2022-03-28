from datetime import datetime
from flask import Flask,request
from suds.client import Client

app = Flask("__name__")
client = Client('http://9346-193-40-12-11.ngrok.io/?wsdl', cache=None)
#client = Client('http://localhost:8090/?wsdl', cache=None)#

# the Ping
@app.route('/')
def index():
    params = request.args.get('domain_name')
    result = client.service.ping_host(params)
    return str(result[0])


@app.route('/showip')
def showip():
    params = request.args.get('domain_name')
    result = client.service.show_ip(params)
    return str(result[0])

@app.route('/showdns')
def showdns():
    params = request.args.get('domain_name')
    result = client.service.show_dns(params)
    if "not" in result:
        return "domain is incorrect"
    else:
        return str(result[0])

if __name__ == "__main__":
    app.run(debug=True)
