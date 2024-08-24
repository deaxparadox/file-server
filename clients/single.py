import requests

filename = r'/home/paradox/Documents/github/file-server/uploads/permute_brackets.py'

url = 'http://127.0.0.1:9000/upload/'
file = {'file': open(filename, 'rb')}
r = requests.post(url=url, files=file) 
print(r.json())