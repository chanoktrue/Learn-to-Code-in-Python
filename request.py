import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
try:
    statusCode = r.status_code
    # result = r.headers
    json = json.loads(r.text)    
    print(json["title"])
except:
    print("error")
