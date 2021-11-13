#!/usr/bin/python

def parse_response(data):
    split_data = data.split(b'\r\n')
    response_code = int(split_data.split(b' ')[1].decode())
    return response_code
