from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, String

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import os
import platform
import subprocess
import netifaces as ni
import shutil
import socket
import dns 
import dns.resolver

class HelloWorldService(ServiceBase):

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """

        for i in range(times):
            yield u'Tere, %s' % name

    @rpc(String, _returns=Iterable(Unicode))
    def ping_host(ctx,host_name):
        returned_result = os.system(f"ping -c 2 {host_name}")
        if returned_result == 0:
            yield "Successful"
        else:
            yield "Domain is Down"

    @rpc(String, _returns=Iterable(Unicode))     
    def show_ip(ctx,host_name):
        returned_result = dns.resolver.query(host_name, 'A')
        for i in returned_result:
            ip_address = i.to_text()
        yield ip_address

application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8090")
    logging.info("wsdl is at: http://localhost:8090/?wsdl")

    server = make_server('127.0.0.1', 8090, wsgi_application)
    server.serve_forever()
