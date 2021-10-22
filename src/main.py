#!/usr/bin/python

import os
import socket
import mimetypes
from tcpserver import *
from httpserver import *



def main():
    server = HTTPServer()
    server.start()


if __name__ == '__main__':
    main()
