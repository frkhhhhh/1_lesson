import requests
import json


url='https://dummyjson.com/users'

answer=requests.get(url)
if answer.status_code==200:
    dt=json.loads(answer.text)

    

    with open("users.txt",'w') as file:
        json.dump(dt["users"][20:30],file, indent=4)


        with open("users.json","w") as json_file:
            json.dump(dt["users"][:5], json_file, indent=4)

