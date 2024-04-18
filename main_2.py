import requests
import json


url='https://dummyjson.com/carts'

response=requests.get(url)
if response.status_code==200:
    data=json.loads(response.text)
    with open("carts.txt","w") as carst_file:
        json.dump(data["carts"][:15],carst_file, indent=4)


#  Json formatidan {dictga} o'zgartirish uchun ......
        
        
        with open("carts.json","w") as c_json_f:
            json.dump(data["carts"][:5],c_json_f,indent=4)
