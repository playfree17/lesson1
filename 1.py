import requests
resparse2 = []
re = requests.get("https://bank.gov.ua/ua/markets/exchangerate-chart?cn%5B%5D=USD")
g = re.text
g.find("$")
# parse3 = j.split("Офіційний курс гривні щодо іноземних валют")
# for parse1 in parse3:
#     if parse1.startswith("$"):
#         for parse_elem_2 in parse1:
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 print(parse3)
