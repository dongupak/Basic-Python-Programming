import requests

r = requests.get('https://github.com/')
print('content-type=',r.headers['content-type'])
print('encoding=',r.encoding)
