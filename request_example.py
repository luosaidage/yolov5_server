import requests

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'file': open('二维码3.jpg;type=image/jpeg', 'rb'),
}

response = requests.post('https://luosaidage-ultralytics-yolov5-64qpqxrph9vg-8000.githubpreview.dev/uploadfile/', headers=headers, files=files)

print (response)