import requests 
r = requests.get("https://www.google0.com")
try:
    statusCode = r.status_code
    print(statusCode)
except:
    print("error")
