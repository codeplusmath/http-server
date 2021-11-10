#!/usr/bin/python

def hfilter(data):
    # [b'HOST: 127.0.0.1:5000']
    filtered_headers = {}
    for d in data:
        tmp = d.decode().split(': ')
        #'HOST' '127.0.0.1:5000'
        if tmp[0]!='HOST':
            filtered_headers[tmp[0]] = tmp[1]
    return filtered_headers

# print(hfilter([b'HOST: 127.0.0.1:5000', b'Connection: keep-alive', b'Content-length: 0']))
