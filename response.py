#!/usr/bin/python

def parse_response(data):
    try:
        response_body = data.split(b'\r\n\r\n')[1]
    except:
        print('No response body')
        response_body = None
    split_data = data.split(b'\r\n')
    response_code = int(split_data.split(b' ')[1].decode())
    print(response_code)
    return response_code, response_body
