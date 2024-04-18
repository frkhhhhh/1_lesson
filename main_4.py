import requests
import json

url='https://dummyjson.com/posts'

rsp=requests.get(url)
if rsp.status_code==200:
    dt=json.loads(rsp.text)
    with open("posts.txt","w") as file:
        json.dump(dt["posts"][15:30], file, indent=4)
        with open("posts.json", "w") as f:
            json.dump(dt["posts"][5:15], f, indent=4)
