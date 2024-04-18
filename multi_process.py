import requests
import time
import multiprocessing
from bs4 import BeautifulSoup
start=time.perf_counter()
urls= [
    'https://docs.python.org/2/py-modindex.html#cap-f',
    'https://docs.python.org/2/search.html?q=urlparse',
    'https://www.khanacademy.org/',
    'https://www.coursera.org/',
    'https://www.edx.org/' 
]
def foo(url):
    try:
        spn=requests.get(url)
        soup=BeautifulSoup(spn.content, 'html.parser')
        text_content=soup.get_text()
        file_name=f'{url.split("/")[-1]}.txt'
        with open(file_name,"w", encoding="UTF-8") as f:
            f.write(text_content)
            print(url)

    except Exception as e:
        print(f"ERROR {url} :{e}")

        print(f'{soup} downloaded')
if __name__=="__main__":
    process=[]


    for url in urls:
        t=multiprocessing.Process(target=foo, args=[url])
        t.start()
        process.append(t)
    
    
    for i in process:
        i.join()

end=time.perf_counter()

print(f'{end-start} Processed')


 



