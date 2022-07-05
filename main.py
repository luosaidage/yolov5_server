from typing import Union

from fastapi import FastAPI, UploadFile,File

from pydantic import BaseModel

import detect
# import ddd_api
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile = File(...)):
    contents = await file.read()
    with open('./images/test.jpg','wb') as f:
        f.write(contents)
    # opt = detect.myoption()
    # detect.check_requirements(exclude=('tensorboard', 'thop'))
    # detect.run(**vars(opt))

    tt = detect
    tt.run()

    with open('det_json/test.jpg.json','r') as rf:
        # data = json.load(rf)
        j_list =  rf.readlines()
        result = []
        for i in j_list:
            result.append(json.loads(i))
            
    return {'filename':file.filename,'result':result}