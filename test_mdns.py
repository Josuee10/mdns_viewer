# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from zeroconf import ServiceBrowser, Zeroconf
from flask_cors import CORS

import socket

app = Flask(__name__)
CORS(app)

class MyListener:
    def __init__(self):
        self.services = []

    def remove_service(self, zeroconf, type, name):
        print("Service {name} removed".format(name=name))
        self.services = [s for s in self.services if s['name'] != name]

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service {name} added, service info: {info}".format(name=name, info=info))
        if info:
            # Usar 'addresses' en lugar de 'address' y convertir la primera dirección IP a una cadena.
            self.services.append({'name': name, 'address': socket.inet_ntoa(info.addresses[0]), 'port': info.port})

    def update_service(self, zeroconf, type, name):
        print("Service {name} updated".format(name=name))

# Aquí están los tipos de servicio que estás buscando.
service_types = [b"_mi-connect._udp.local.", b"_smb._tcp.local."]

listener = MyListener()
zeroconf = Zeroconf()

for service_type in service_types:
    browser = ServiceBrowser(zeroconf, service_type.decode('utf-8'), listener)

@app.route('/hosts', methods=['GET'])
def get_hosts():
    return jsonify(listener.services), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
