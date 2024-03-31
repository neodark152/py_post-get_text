import requests

# Enter the telebot token and chatid
bot_token = '6863952265:AAF0TV0lH3sOIg62AM51hp7sCIudmsj9Tb4'
chat_id = '6726678830'

# url1 for get video metadate in BiliBili, url2 for send message via telegream
url1 = "https://api.bilibili.com/x/web-interface/ranking/v2"
url2 = f'https://api.telegram.org/bot{bot_token}/sendMessage'

params = {"tid" : "1"}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

message = ""

res1 = requests.get(url1, params=params, headers=headers)

if res1.status_code == 200:
  message ="The top ranked video on bilibili is: " + res1.json()["data"]["list"][0]["title"]


data_ = {
    'chat_id': chat_id,
    'text': message
}

res2 = requests.post(url2, data=data_)

print(res2.text)