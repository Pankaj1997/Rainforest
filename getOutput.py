#use Python2.7 to run
import requests

def addDotJson(url):
    if "?" in url:
       substr = "?"
    else:
        return url + ".json"
    idx = url.index(substr)
    new_url = url[:idx] + ".json" + url[idx:]
    return new_url

def getResponse(url):
    response = requests.get(url)
    r = response.json()
    print r
    return r


url = "https://www.letsrevolutionizetesting.com/challenge"
msg = "This is not the end"
new_url = str(addDotJson(url))
while msg == "This is not the end":
    response = getResponse(new_url)
    msg = response['message']
    if msg != "This is not the end":
        break
    url = response['follow']
    new_url = str(addDotJson(url))
