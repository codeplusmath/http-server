#!/usr/bin/python
import unittest
import requests
import os
import socket

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

'''

class TestPutRequest(unittest.TestCase):
    def Test_Put_txtfile(self):
        
    def Test_Put_pngfile(self):
    
    def Test_Put_htmlfile(self):
    
    def Test_Put_mp3file(self):
    
    def Test_Put_pdffile(self):
    
    def Test_Put_pyfile(self):
    
    def Test_Put_jsfile(self):
    
    def Test_Put_cssfile(self):
    
    def Test_Put_204(self):
    
    def Test_Put_201(self):



class TestPostRequest(unittest.TestCase):
    def test_Post_txtfile(self):
    
    def test_Post_pngfile(self):
    
    def test_Post_htmlfile(self):
    
    def test_Post_mp3file(self):
    
    def test_Post_pdffile(self):
    
    def test_Post_pyfile(self):
    
    def test_Post_jsfile(self):
    
    def test_Post_cssfile(self):
    
    def test_Post_201(self):
    
    def test_Post_403(self):
    
    def test_Post_urlencoded(self):
    
    def test_Post_multipart(self):

'''
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


class TestInvalidRequest(unittest.TestCase):
    def test_Invalid(self):
        req_headers = GetDictFile('invalid_req.txt')
        r = requests.patch('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 501)


if __name__ ==  '__main__':
    unittest.main()

