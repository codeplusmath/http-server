#!/usr/bin/python
import unittest
import requests
import os
import socket
import gzip
def GetDictFile(filename):
    f = open(f'./testfiles/{filename}', 'r')
    data = f.readlines()[1:]
    header_data = {}
    for line in data:
        words = line.split(': ')
        header_data[words[0]] = words[1].strip('\n')

    f.close()
    return header_data


class TestGetRequest(unittest.TestCase):
 
    def test_Get_txtfile(self):        
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.txt', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.txt', 'wb')
        f.write(r.content)
        f.close()

    def test_Get_pngfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.png', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.png', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.png'))

    def test_Get_htmlfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/index.html', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/index.html'))

    def test_Get_htmlcookie(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/login.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/login.html', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/index.html'))

    def test_Get_htmlfilecookie(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/login.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/afterlogin.html', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/index.html'))

    def test_Get_audiofile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.wav', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.wav', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.wav'))

    def test_Get_pdffile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.pdf', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.pdf', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.pdf'))

    def test_Get_pyfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.py', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.py', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.py'))

    def test_Get_jsfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.js', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.js', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.js'))

    def test_Get_cssfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.css', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.css', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.css'))

    def test_Get_404(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/notfound.txt', headers = req_headers)
        self.assertEqual(r.status_code, 404)

'''
class TestHeadRequest(unittest.TestCase):    
    def test_Head_txtfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.head('http://127.0.0.1:8888/test.txt', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_pngfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.png', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_htmlfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_audiofile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.wav', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_pdffile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.pdf', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_pyfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.py', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_jsfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.js', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def test_Head_cssfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.css', headers = req_headers)
        self.assertEqual(r.status_code, 200)
    
    def test_Head_404(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/notfound.txt', headers = req_headers)
        self.assertEqual(r.status_code, 404)


class TestPutRequest(unittest.TestCase):
    def test_Put_txtfile(self):
        req_headers = GetDictFile('put_req.txt')
        f = open('./clientrecvfiles/testput.txt', 'rb')
        data = f.read()        
        r = requests.put('http://127.0.0.1:8888/Upload/testput.txt', headers = req_headers, data = data)
        print(r)
        f.close()
        print('file closed')
        self.assertEqual(r.status_code, 201)

    def test_Put_204(self):
        req_headers = GetDictFile('put_req.txt')
        f = open('./clientrecvfiles/testput.txt', 'rb')
        data = f.read()
        r = requests.put('http://127.0.0.1:8888/Upload/testput.txt', headers = req_headers, data)
        f.close()
        self.assertEqual(r.status_code, 204)

    def test_Put_403(self):
        req_headers = GetDictFile('put_req.txt')
        f = open('./clientrecvfiles/testput.txt', 'rb')
        data = f.read()
        r = requests.put('http://127.0.0.1:8888/Upload/readonly.txt', headers = req_headers, data)
        f.close()
        self.assertEqual(r.status_code, 403)


class TestPostRequest(unittest.TestCase):
    
    def test_Post_txtfile(self):
        req_headers = GetDictFile('post_req.txt')
        f = open('./clientrecvfiles/testpost.txt', 'rb')
        data = f.read()
        r = requests.post('http://127.0.0.1:8888/Upload/testpost.txt', headers = req_headers, data = data)
        f.close()
        self.assertEqual(r.status_code, 201)

    def test_Post_403(self):
        req_headers = GetDictFile('post_req.txt')
        f = open('./clientrecvfiles/testpost.txt', 'rb')
        data = f.read()
        r = requests.post('http://127.0.0.1:8888/Upload/readonly.txt', headers = req_headers, data = data)
        f.close()
        self.assertEqual(r.status_code, 403)
    
    def test_Post_urlencoded(self):
        req_headers = GetDictFile('post_req.txt')
        f = open('./clientrecvfiles/testpost.txt', 'rb')
        r = requests.post('http://127.0.0.1:8888/Upload/testurlencoded.txt', headers = req_headers, data = data)
        self.assertEqual(r.status_code, 201)
    
    def test_Post_multipart(self):
        req_headers = GetDictFile('post_req.txt')
        f = open('./clientrecvfiles/testpost.txt', 'rb')
        r = requests.post('http://127.0.0.1:8888/Upload/testmultipart.txt', headers = req_headers, data = data)
        self.assertEqual(r.status_code, 201)



class TestDeleteRequest(unittest.TestCase):
    def test_Delete_txtfile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.txt', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_pngfile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.png', headers = req_headers)
        self.assertEqual(r.status_code, 204)
    
    def test_Delete_htmlfile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.html', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_audiofile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.wav', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_pdffile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.pdf', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_pyfile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.py', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_jsfile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.js', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_cssfile(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/test1.css', headers = req_headers)
        self.assertEqual(r.status_code, 204)

    def test_Delete_403(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/readonly.txt', headers = req_headers)
        self.assertEqual(r.status_code, 403)
    
    def test_Delete_404(self):
        req_headers = GetDictFile('delete_req.txt')
        r = requests.delete('http://127.0.0.1:8888/anything.txt', headers = req_headers)
        self.assertEqual(r.status_code, 404)
'''

class TestInvalidRequest(unittest.TestCase):
    def test_Invalid(self):
        req_headers = GetDictFile('invalid_req.txt')
        r = requests.patch('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 501)


if __name__ ==  '__main__':
    unittest.main()

