import requests
from  concurrent.futures import ProcessPoolExecutor



files = [
    r"/home/paradox/Downloads/Doguhan Uluca - Angular for Enterprise Applications_ Build scalable Angular apps, 3rd Edition-Packt Publishing (2024).pdf",
    r"/home/paradox/Downloads/Lamis Chebbi - Reactive Patterns with RxJS and Angular Signals_ Elevate your Angular 18 applications with RxJS Observables, 2nd Edition-Packt Publishing (2024).pdf",
    r"/home/paradox/Downloads/Learning_Python.pdf",
    r"/home/paradox/Downloads/[O`Reilly] - Programming Python, 4th ed. - [Lutz].pdf ( PDFDrive ).pdf",
    r"/home/paradox/Downloads/Gaurav Agarwal - Modern DevOps Practices_ Implement, secure, and manage applications on the public cloud by leveraging cutting-edge tools-Packt Publishing (2024).pdf",
    r"/home/paradox/Downloads/Algorithms_ Design Techniques and Analysis ( PDFDrive ).pdf",
    r"/home/paradox/Downloads/Deepak Vohra - Kubernetes Microservices with Docker-Apress (2016).pdf",    
]

url = 'http://127.0.0.1:9000/u/'

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