import requests


def get_flag():
    return "flag"

def push_flag(token,ip,flag):
    url = "https://10.10.10.10/pushFlag?token=%s&ip=%s&flag=%s"
    r = requests.get(url)
    return r.json()
