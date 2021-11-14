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
    def Test_Get_txtfile(self):        
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.txt', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.txt', 'wb')
        f.write(r.content)
        f.close()


    def Test_Get_pngfile(self):    
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.png', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.png', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.png'))

    def Test_Get_htmlfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/index.html', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/index.html'))

    def Test_Get_htmlfilecookie(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/index.html', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/index.html'))

    def Test_Get_audiofile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.wav', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.wav', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.wav'))

    def Test_Get_pdffile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.pdf', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.pdf', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.pdf'))

    def Test_Get_pyfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.py', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.py', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.py'))

    def Test_Get_jsfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.js', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.js', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.js'))

    def Test_Get_cssfile(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.css', headers = req_headers)
        self.assertEqual(r.status_code, 200)
        f = open('./clientrecvfiles/test.css', 'wb')
        f.write(r.content)
        f.close()
        self.assertTrue(os.path.exists('./clientrecvfiles/test.css'))

    def Test_Get_404(self):
        req_headers = GetDictFile('get_req.txt')
        r = requests.get('http://127.0.0.1:8888/notfound.txt', headers = req_headers)
        self.assertEqual(r.status_code, 404)
        print(r.content)


class TestHeadRequest(unittest.TestCase):    
    def Test_Head_txtfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.head('http://127.0.0.1:8888/test.txt', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_pngfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.png', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_htmlfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_audiofile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.wav', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_pdffile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.pdf', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_pyfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.py', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_jsfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.js', headers = req_headers)
        self.assertEqual(r.status_code, 200)

    def Test_Head_cssfile(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/test.css', headers = req_headers)
        self.assertEqual(r.status_code, 200)
    
    def Test_Head_404(self):
        req_headers = GetDictFile('head_req.txt')
        r = requests.get('http://127.0.0.1:8888/notfound.txt', headers = req_headers)
        self.assertEqual(r.status_code, 200)

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
    def Test_Post_txtfile(self):

    def Test_Post_pngfile(self):

    def Test_Post_htmlfile(self):

    def Test_Post_mp3file(self):

    def Test_Post_pdffile(self):

    def Test_Post_pyfile(self):

    def Test_Post_jsfile(self):

    def Test_Post_cssfile(self):

    def Test_Post_201(self):

    def Test_Post_403(self):
    
    def Test_Post_urlencoded(self):
    
    def Test_Post_multipart(self):

class TestDeleteRequest(unittest.TestCase):
    def Test_Delete_txtfile(self):

    def Test_Delete_pngfile(self):

    def Test_Delete_htmlfile(self):

    def Test_Delete_mp3file(self):

    def Test_Delete_pdffile(self):

    def Test_Delete_pyfile(self):

    def Test_Delete_jsfile(self):

    def Test_Delete_cssfile(self):

    def Test_Delete_202(self):

    def Test_Delete_204(self):

    def Test_Delete_404(self):


class TestInvalidRequest(unittest.TestCase):
    def Test_Invalid(self):
        req_headers = GetDictFile('invalid_req.txt')
        r = requests.patch('http://127.0.0.1:8888/index.html', headers = req_headers)
        self.assertEqual(r.status_code, 501)
        



if __name__ ==  '__main__':
    unittest.main()

