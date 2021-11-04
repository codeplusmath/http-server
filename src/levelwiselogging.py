#!/usr/bin/python

Users = {'Normal':0, 'Admin':1, 'Developer':2}

class levelwiselogging():
    self.configfile = 'usr.config'
    self.usertype = self.getUserType()
    self.logfile = 'logs.log'

    def getUserType(self):
        with open(self.configfile, 'r') as fileobj:
            for line in fileobj:
                words = line.strip(' = ')
                for w in words:
                    if w == 'USER':
                        return Users[words[1]]
                    else:
                        return 0

    def lPrint(self, level, tup):
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
            print('Error: 0x002\nIncorrect user type\n')
            return 1
