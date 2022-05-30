
import requests
responce = requests.get("https://coinmarketcap.com")
responce_text = (responce.text)
responce_parse = responce_text.split("<span>")
for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        print(parse_elem_1)









# import requests
# re = requests.post("https://httpbin.org/post",data="Test one",headers={"h1":"Test title"})
# print(re.text)







# import requests
# re = requests.get("https://httpbin.org/get")
# print(re.text)
# print(f"Datatype - {type(re.text)}")

# import urllib.request
# opener = urllib.request.build_opener()
# res = opener.open("https://httpbin.org/get")
# print(res.read())