from fastapi import FastAPI, UploadFile,File

from pathlib import Path
import det_api
import json
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/detect/")
async def create_upload_file(file:UploadFile = File(...)):
    try:
        os.mkdir('./images')
        os.remove("./images/test.jpg")
        os.remove("det_json/test.jpg.json")
    except:
        pass
        
    contents = await file.read()
    with open('./images/test.jpg','wb') as f:
        f.write(contents)

    yolo = det_api
    yolo.run()
    result = []
    if Path('det_json/test.jpg.json').exists():
        with open('det_json/test.jpg.json','r') as rf:
            # data = json.load(rf)
            j_list = rf.readlines()
            for i in j_list:
                result.append(json.loads(i))
            
    return {'filename':file.filename,'result':result}
