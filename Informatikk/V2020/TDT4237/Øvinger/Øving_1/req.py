import requests

s = "Connection: keep-alive\nContent-Length: 56\nCache-Control: max-age=0\nOrigin: https://molde.idi.ntnu.no:8037\nUpgrade-Insecure-Requests: 1\nContent-Type: application/x-www-form-urlencoded\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36\nSec-Fetch-User: ?1\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\nSec-Fetch-Site: same-origin\nSec-Fetch-Mode: navigate\nReferer: https://molde.idi.ntnu.no:8037/login\nAccept-Language: en-GB,en-US;q=0.9,en;q=0.8\nHost: molde.idi.ntnu.no:8037".split(
    "\n")
url = "http://molde.idi.ntnu.no:8037/login"

data = {
    'username': 'Sander',
    'password': '12345678'
}

x = requests.post(url, data=data)

print(x.text)
