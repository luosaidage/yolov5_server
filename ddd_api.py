import json
with open('det_json/test.jpg.json','r') as rf:
    # data = json.load(rf)
    j_list =  rf.readlines()
    result = []
    for i in j_list:
        result.append(json.loads(i))

    print (result)