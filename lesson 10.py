import urllib.request
opener = urllib.request.build_opener()
res = opener.open("https://httpbin.org/get")
print(res.read())