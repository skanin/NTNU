import json
import requests
import hashlib

response = requests.get("https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-hashchain.json")
f = json.loads(response.text)


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


def msg(lst, hash, str):
    if len(str) == len(lst):
        return str

    for elem in lst:

        if computeMD5hash(hash + elem["ch"]) == elem["hash"]:
            str += elem["ch"]
            
            return msg(lst, computeMD5hash(hash + elem["ch"]), str)

    return str


#print(computeMD5hash("julekalender"))
print(msg(f, computeMD5hash("julekalender"), ""))