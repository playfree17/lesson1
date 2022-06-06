import requests
res_parse_list = []
responce = requests.get("https://coinmarketcap.com")
responce_text = (responce.text)
responce_parse = responce_text.split("<span>")
for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
               # res_parse_list.append(parse_elem_2)
                print(parse_elem_1)
# bitcoin_ex = res_parse_list[0]
# Ef = res_parse_list[1]
# print("btc - ",bitcoin_ex)
# print("eth - ",Ef)








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