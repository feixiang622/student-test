import json


datafile = 'data.json'

def file_mana(datafile, default={}):
    try:
        with open(datafile) as d:
            # print(json.load(d))
            return json.load(d)
    except FileNotFoundError:
        print("没有发现相关文件")
        return default

def wirte_json(datafile, data):
    with open(datafile, 'w') as d:
         json.dump(data, d)



