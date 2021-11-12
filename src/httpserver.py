#!/usr/bin/python

import os
import socket
import mimetypes
from tcpserver import *
from datetime import datetime
import cookies
from linecache import getline
import hashlib

global cookie_status_flag
cookie_status_flag = 0

class HTTPServer(TCPServer):

    headers = {
        'Server': 'CNServer',
        'Content-Type': 'text/html',
    }

    status_codes = {
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented',
        202: 'Accepted',
        204: 'No Content',
        201: 'Created',
        403: 'Forbidden',
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
            content_type = mimetypes.guess_type(path)[0] + '; charset=utf-8' or 'text/html' + '; charset=utf-8'
            stat = os.stat(path)
            last_modified = datetime.fromtimestamp(stat.st_mtime).strftime('%d %b %Y %H:%M:%S GMT')
            with open(path, 'rb') as f:
                response_body = f.read()
                md5 = hashlib.md5(response_body).hexdigest()
                f.close()
            
            content_length = len(response_body)
            extra_headers = {'Content-Length': content_length, 'Content-Type': content_type, 'Content-Encoding': 'gzip', 'Last-Modified': last_modified, 'Content-md5': md5}

        else:
            response_line = self.response_line(404)
            response_body = b'<h1>404 Not Found</h1>'
            content_length = len(response_body)
            md5 = hashlib.md5(response_body).hexdigest()
            extra_headers = {'Content-Length': content_length, 'Content-Type': 'text/html; charset=utf-8', 'Content-Encoding': 'gzip', 'Content-md5': md5}

        cookie_string = 'cookie'

        if request.other_headers.has_key('cookie') and os.path.exists(f'../cookies/{request.other_headers[cookie_string]}'):
            edate = datetime.date(getline(f'../cookies/{request.other_headers[cookie_string]}', 2).strip('\n'))

            if edate - datetime.now() >=0:
                cookie_status_flag = 1
                path = './www/' + 'afterlogin.html'    
                with open(path, 'rb') as f:
                    response_body = f.read()
                    f.close()
 
            else:
                os.remove(f'../cookies/{request.other_headers[cookie_string]}')
                cookie_header = cookies.setcookie('./www/login.html')
                c = self.other_headers.pop('cookie')
        
        elif path == './www/login.html':
            cookie_header = cookies.setcookie(path)
            c = self.other_headers.pop('cookie')

        else:
            pass

        today = datetime.now()
        d1 = "Date: " + today.strftime('%a') + ', '
        d1 += today.strftime("%d %b %Y %H:%M:%S GMT")
        d1 = d1.encode()

        response_headers = self.response_headers(extra_headers)
        other_headers = self.response_headers(request.other_headers)
        blank_line = b'\r\n'
        response = b''.join([response_line, response_headers, d1, blank_line, other_headers, blank_line, response_body])
        return response
    
    
    def handle_HEAD(self, request):
        path = './www/' + request.uri.strip('/')

        if not path:
            path = './www/' + 'index.html'

        if os.path.exists(path) and not os.path.isdir(path):
            response_line = self.response_line(200)
            content_type = mimetypes.guess_type(path)[0] + '; charset=utf-8' or 'text/html' + '; charset=utf-8'

            content_length = os.path.getsize(path)
            response_body = b''
            extra_headers = {'Content-Length': content_length, 'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

        else:
            response_line = self.response_line(404)
            response_body = b'<h1>404 Not Found</h1>'
            md5 = hashlib.md5(response_body).hexdigest()
            extra_headers = {'Content-Length': content_length, 'Content-Type': 'txt/html; charset=utf-8', 'Content-Encoding': 'gzip', 'Content-md5': md5}
            response_headers = self.response_headers(extra_headers)

        today = datetime.now()
        d1 = "Date: " + today.strftime('%a') + ', '
        d1 += today.strftime("%d %b %Y %H:%M:%S GMT")
        d1 = d1.encode()
        
        other_headers = self.response_headers(request.other_headers)
        blank_line = b'\r\n'
        response = b''.join([response_line, response_headers, d1, blank_line, other_headers, blank_line, response_body])
        return response


    def handle_DELETE(self, request):
        path = './www/' + request.uri.strip('/')
        
        if os.path.exits(path):
            if(os.access(path, os.W_OK)):
                os.remove(path)
                response_line = self.response_line(200)
                response_body = "<html><body><h1>File deleted.</h1></body></html>"
                md5 = hashlib.md5(response_body).hexdigest()
                extra_headers = {'Content-Length': content_length, 'Content-Type': 'txt/html; charset=utf-8', 'Content-Encoding': 'gzip', 'Content-md5': md5}
                response_headers = self.response_headers(extra_headers)

            else:
                response_headers = self.response_headers()
                if(os.path.exits(absolute_path)):
                    response_line = self.response_line(202)
                    response_body = ""
                else:
                    response_line = self.response_line(204)
                    response_body = ""
                    
        else:
            response_headers = self.response_headers()
            response_line = self.response_line(404)
          
        today = datetime.now()
        response_body = response_body.encode()
        d1  = today.strftime('%a') + ', ' + today.strftime("%d %b %Y %H:%M:%S GMT")
        response_fields = "Date: %s\r\n" %(d1)
        response_fields = response_fields.encode()
        breakline = b'\r\n'
        other_headers = self.response_headers(request.other_headers)
        response = b"".join([response_line, response_headers, response_fields, other_headers, breakline, response_body])
        return response
    

    def handle_PUT(self, request):
        path = './www/' + request.uri.strip('/')
        data = request.request_data
        if os.path.exists(path):
            #updated but entity body not returned
            response_line = self.response_line(204)
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
        other_headers = self.response_headers(request.other_headers)
        response = b"".join([response_line , d1 , other_headers, breakline , uri])
        return response

    def handle_POST(self, request):
        path = './www/' + request.uri.strip('/')
       	#data = requests.request_data
        if(request.other_headers["Content-Type"] == "application/x-www-form-urlencoded"):
            data = request.request_data.split('&')

        elif(request.other_headers["Content-Type"].split(';')[0] == "multipart/form-data"):
            separator = request.other_headers["Content-Type"].split(';')[1]
            raw_data = request.request_data.split(f'--{separator}')
            data = ''
            for x in range(1, len(raw_data)-1):    
                d = raw_data[x].split('; ')
                for y in range(1, len(d)):
                    data += d[y].replace('\r\n', ' ') 
        else:
            data = request.request_data

        if os.path.exists(path):
            try:
                words = request.uri.split('(')
                count = int(words[1][0])
                count += 1
                path = words[0] + '(' + str(count) + words[1:]
            except:
                words = request.uri.split('.')
                path = words[0] + ' (1)' + words[1]

            response_line = self.response_line(403)
            #content type checking 
            fp = open(path, 'wb')
            for line in data:
                fp.writelines(line)
            fp.close()
    	
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
    
        other_headers = self.response_headers(request.other_headers)
        uri = request.uri.encode()
        response = b"".join([response_line , d1 , other_headers, breakline , uri])
        return response


    def HTTP_501_handler(self, request):
        response_line = self.response_line(status_code=501)
        response_headers = self.response_headers()
        blank_line = b'\r\n'
        response_body = b'<h1>501 Not Implemented</h1>'
        
        other_headers = self.response_headers(request.other_headers)

        return b"".join([response_line, response_headers, other_headers, blank_line, response_body])


