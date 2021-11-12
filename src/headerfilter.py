#!/usr/bin/python

def hfilter(data):
    # [b'HOST: 127.0.0.1:5000']
    filtered_headers = {}
    avoid_headers = [b'Host', b'Accept-Encoding', b'Accept-Language', b'Accept', b'User-Agent']
    for d in data:
        tmp = d.decode().split(': ')
        #'HOST' '127.0.0.1:5000'
        if tmp[0] not in avoid_headers:
            filtered_headers[tmp[0]] = tmp[1]
        
    return filtered_headers

# print(hfilter([b'HOST: 127.0.0.1:5000', b'Connection: keep-alive', b'Content-length: 0']))
