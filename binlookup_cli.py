import requests

binn = '4673302112'
# binn = input("enter bin: ")
# API = "https://lookup.binlist.net/{}".format(binn)
binn = binn[:5]
print(binn)
# resp = requests.get(API)
# resp_json = resp.json()
# print(resp.content)
# number_length = resp_json['number']['length']
# number_luhn = resp_json['number']['luhn']
# print("number_length:{}\nnumber_luhn:{}".format(number_length,number_luhn))
# scheme = resp_json['scheme']
# typee = resp_json['type']
# brand = resp_json['brand']
# prepaid = resp_json['prepaid']
# print("scheme:{}\ntype:{}")
# # country
# country_numeric = resp_json['country']['numeric']
# country_alpha2 = resp_json['country']['alpha2']
# country_name = resp_json['country']['name']
# country_emoji = resp_json['country']['emoji']
# country_currency = resp_json['country']['currency']
# country_latitude = resp_json['country']['latitude']
# country_longitude = resp_json['country']['longitude']

# #bank
# bank_name = resp_json['bank']['name']
# bank_url = resp_json['bank']['bank_url']
# bank_phone = resp_json['bank']['phone']
# bank_city = resp_json['bank']['city']



# {"number":{"length":16,"luhn":true},"scheme":"visa","type":"debit","brand":"Visa/Dankort","prepaid":false,"country":{"numeric":"208","alpha2":"DK","name":"Denmark","emoji":"🇩🇰","currency":"DKK","latitude":56,"longitude":10},"bank":{"name":"Jyske Bank","url":"www.jyskebank.dk","phone":"+4589893300","city":"Hjørring"}}
