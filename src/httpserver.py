#!/usr/bin/python

import os
import socket
import mimetypes
from tcpserver import *
from datetime import datetime


class HTTPServer(TCPServer):

    headers = {
        'Server': 'CrudeServer',
        'Content-Type': 'text/html',
    }

    status_codes = {
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented',
        202: 'Accepted'
        204: 'No Content',
        201: 'Created'
    }

    
    def handle_request(self, data):
        request = HTTPRequest(data)

        try:
            handler = getattr(self, 'handle_%s' % request.method)
        except AttributeError:
            handler = self.HTTP_501_handler

        response = handler(request)
        return response


    def response_line(self, status_code):
        reason = self.status_codes[status_code]
        response_line = 'HTTP/1.1 %s %s\r\n' % (status_code, reason)
        return response_line.encode() 


    def response_headers(self, extra_headers=None):
        headers_copy = self.headers.copy() 
        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ''

        for h in headers_copy:
            headers += '%s: %s\r\n' % (h, headers_copy[h])

        return headers.encode() 


    def handle_OPTIONS(self, request):
        response_line = self.response_line(200)
        extra_headers = {'Allow': 'OPTIONS, GET'}
        response_headers = self.response_headers(extra_headers)

        blank_line = b'\r\n'
        return b''.join([response_line, response_headers, blank_line])

    
    def handle_GET(self, request):
        path = './www/' + request.uri.strip('/') 

        if not path:
            path = './www/' + 'index.html'

        if os.path.exists(path) and not os.path.isdir(path): 
            response_line = self.response_line(200)
            content_type = mimetypes.guess_type(path)[0] or 'text/html'
            
            with open(path, 'rb') as f:
                response_body = f.read()
                f.close()

            content_length = len(response_body)
            extra_headers = {'Content-Length': content_length, 'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

        else:
            response_line = self.response_line(404)
            response_headers = self.response_headers()
            response_body = b'<h1>404 Not Found</h1>'

        blank_line = b'\r\n'
        response = b''.join([response_line, response_headers, blank_line, response_body])
        return response
    
    
    def handle_HEAD(self, request):
        path = './www/' + request.uri.strip('/')

        if not path:
            path = './www/' + 'index.html'

        if os.path.exists(path) and not os.path.isdir(path):
            response_line = self.response_line(200)
            content_type = mimetypes.guess_type(path)[0] or 'text/html'

            content_length = os.path.getsize(path)
            response_body = b''
            extra_headers = {'Content-Length': content_length, 'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

        else:
            response_line = self.response_line(404)
            response_headers = self.response_headers()
            response_body = b'<h1>404 Not Found</h1>'

        blank_line = b'\r\n'
        response = b''.join([response_line, response_headers, blank_line, response_body])
        return response


    def handle_DELETE(self, request):
        path = './www/' + request.uri.strip('/')
        
        if os.path.exits(path):
            try:
                os.remove(path)
                response_line = self.response_line(200)
                response_body = "<html><body><h1>File deleted.</h1></body></html>"

            except:
                if(os.path.exits(absolute_path)):
                    response_line = self.response_line(202)
                    response_body = ""
                else:
                    response_line = self.response_line(204)
                    response_body = ""
                    
        else:
            response_line = self.response_line(404)
          
        today = datetime.now()
        response_body = response_body.encode()
        d1  = today.strftime('%a') + ', ' + today.strftime("%d %b %Y %H:%M:%S GMT")
        response_fields = "Date: %s\r\n" %(d1)
        response_fields = response_fields.encode()
        breakline = b'\r\n'
        response = b"".join([response_line, breakline, response_fields, response_body])
        return response
    

    def handle_PUT(self, request):
    
        path = './www/' + request.uri.strip('/')
        data = requests.request_data
        if os.path.exists(path):
                #updated but entity body not returned
                response-line = self.response_line(204)
                #overwrite file
                fr = open(path, 'wb')
                for line in data:
                        fr.writelines(line)
                fr.close()

        else:
                response_line = self.response_line(201)
                f1 = open(path, 'wb')
                for line in data:
                    f1.writelines(line)
                f1.close()

        #Sun, 06 Nov 1994 08:49:37 GMT
        today = datetime.now()
        d1 = "Date: " + today.strftime('%a') + ', '
        d1 += today.strftime("%d %b %Y %H:%M:%S GMT")
        d1 = d1.encode()
        breakline = b'\r\n'
    
        uri = request.uri.encode()
        response = b"".join([response_line , d1 , breakline , uri])
        return response


    def HTTP_501_handler(self, request):
        response_line = self.response_line(status_code=501)
        response_headers = self.response_headers()
        blank_line = b'\r\n'
        response_body = b'<h1>501 Not Implemented</h1>'

        return b"".join([response_line, response_headers, blank_line, response_body]


