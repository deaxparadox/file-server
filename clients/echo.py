import requests
from  concurrent.futures import ProcessPoolExecutor


MAX_REQUEST = 10000


url = 'http://127.0.0.1:9000/u/'

def upload(url):
    r = requests.get(url=url) 
    return r.json()


def main():
    with ProcessPoolExecutor() as executor:
        for index, json in enumerate(executor.map(upload, [url] * MAX_REQUEST)):
            # print(index, json)
            ...
            
if __name__ == "__main__":
    main()