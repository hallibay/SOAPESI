from suds.client import Client

client = Client('https://a907-193-40-13-162.ngrok.io/?wsdl', cache=None)

# print(client.service.say_hello(u'Maarika', 5))
#print("Running Service 1 ...")
print(client.service.ping_host("www.googele.com"))
#print("Running Service 2 ...")
#print(client.service.res_name('www.google.com'))
#print("\nRunning Service 3 ...")
#print(client.service.disk_usage('/home'))

# wsdl = Client('http://www.learnwebservices.com/services/hello?wsdl', cache=None)
# request = {'Name': 'Maarika'}
# print(wsdl.service.SayHello(request))
