import requests
import json

url='https://dummyjson.com/products'


response=requests.get(url)
if response.status_code==200:
    data=json.loads(response.text)
    with open("products.txt", 'w') as product_file:
        json.dump(data["products"][:10], product_file, indent=4)

        with open("products.json","w") as product_f:
            json.dump(data["products"][:5], product_f, indent=4)
 

 
 
            with open("carts.json","r") as dict_file:
                modify=json.load(dict_file)
            print(modify)

