import json

def read_json(data_id):
    data_name = "data" + data_id
    file = open('../Data/data.json')
    data = json.load(file)

    for i in data['data']:
        if i["name"] == data_name:
            value = i['content']
            file.close()
            return value
    file.close()
    raise Exception("No such data found.")
