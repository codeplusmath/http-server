#!/usr/bin/python
import sys

sys.path.append('../config/')
from config import USER
Users = {'Normal':0, 'Admin':1, 'Developer':2}

class levelwiselogging:
    def __init__(self):
        self.configfile = '../config/config.py'
        self.usertype = Users[USER]
        self.logfile = '../logs/log.txt'


    def lprint(self, level, tup):
        if level == self.usertype:
            try:
                f = open(self.logfile, 'a')
                final = ''
                for t in tup:
                    final += str(t)
                f.write(final)
                f.close()
            except:
                print('Error: 0x001\nCan\'t append log to file\n')
            return 0
        else:
            pass
            return 1
