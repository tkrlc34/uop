import requests
import sys

user = input('phone_number -> ')


url = "https://api.jahez.net/v2/auth/wallet/m_walletBalance?userName=966"+user


payload = ""
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "X-Parse-Installation-Id": "25cfde8f-7204-434e-a7fb-dde295ee4f70", 
    "User-Agent": "Jahez/2 CFNetwork/1206 Darwin/20.1.0", 
    "Connection": "close", 
    "X-Parse-Application-Id": "RTE8CXsUiVWfG1XlXOyJAxfonvt", 
    "Host": "api.jahez.net", 
    "Accept-Encoding": "gzip, deflate", 
    "Upgrade-Insecure-Requests": "1", 
    "Accept-Language": "en-US,en;q=0.9", 
    "X-Parse-Client-Version": "i1.17.3", 
    "Authorization": "Bearer f271bb38-cdeb-41d4-98eb-8577af29f2bf", 
    "X-Parse-OS-Version": "12.9 (saud)"
}

response = requests.request("GET", url, data=payload, headers=headers)

print("")

print('---------------------')
print(response.text)
