#!/usr/bin/python
import socket
import sys
import logging

global USER
USER = sys.argv[0] or 0


class TCPServer:
    def __init__(self, host = '127.0.0.1', port = 8888):
        self.host = host
        self.port = port

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen()
        #myprint(0, ("Listening at", s.getsockname(),))

        while True:
            conn, addr = s.accept()
            #myprint(1, ("Connected by", addr,))
            data = conn.recv(8192)
            response = self.handle_request(data)
            conn.sendall(response)
            conn.close()

		
class HTTPRequest:

    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = '1.1' 
        self.request_data = ''
        self.parse(data)

    def parse(self, data):
        lines = data.split(b'\r\n')
        request_line = lines[0]
        request_parts = data.split(b'\r\n\r\n')
        try:
            self.request_data = request_parts[1]
        except:
            print('No-Content')

        words = request_line.split(b' ') 

        self.method = words[0].decode() 

        if len(words) > 1:
            self.uri = words[1].decode() 

        if len(words) > 2:
            self.http_version = words[2]
