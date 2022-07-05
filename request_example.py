import re
import requests

def pick_img(path='/Users/sai/Pictures/INT01P07051119.jpg'):
    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'file': open(path, 'rb'),
    }

    response = requests.post('http://47.99.45.195:8000/uploadfile/', headers=headers, files=files, timeout=5)

    print (response.text)
    return response.text