import requests
re = requests.get("https://httpbin.org/get")
print(re.content)
print(f"Datatype - {type(re.text)}")

# import urllib.request
# opener = urllib.request.build_opener()
# res = opener.open("https://httpbin.org/get")
# print(res.read())