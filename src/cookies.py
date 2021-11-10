import random
from datetime import datetime, timedelta
def set_cookie(path):
    cookie_id = random.randint(1000, 50000)
    expire_date = datetime.now() + timedelta(days=10)
    d1 = expire_date.strftime('%a') + ', '
    d1 += expire_date.strftime("%d-%b-%Y %H:%M:%S GMT")
    #expiration time not added
    cookie = 'set-cookie: id={}; expires={}; path={}; domain=\'localhost\'\r\n'.format(cookie_id, d1, path)
    
    cookie_path = f'../cookies/{cookie_id}'
    f = open(cookie_path, 'w')
    f.write(str(cookie_id) + '\n')
    f.write(str(expire_date) + '\n')
    f.write(path)
    f.close()
    
    return cookie.encode()
