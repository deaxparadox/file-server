import requests
from  concurrent.futures import ProcessPoolExecutor


filename1 = r'/home/paradox/Documents/github/file-server/uploads/permute_brackets.py'
filename2 = r"/home/paradox/Downloads/Python for Probability, Statistics, and Machine Learning ( PDFDrive ).pdf"
url = 'http://127.0.0.1:9000/upload/'
files = [filename1] * 1001

def upload(file, url=url):
    uploadfile = {'file': open(file, 'rb')}
    r = requests.post(url=url, files=uploadfile) 
    return r.json()


def main():
    with ProcessPoolExecutor() as executor:
        for index, json in enumerate(executor.map(upload, files)):
            print(index, json)
            
if __name__ == "__main__":
    main()