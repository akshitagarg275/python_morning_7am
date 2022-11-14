import json , requests

def fetch_data(url):
    try:
        data = get_response(url)
        json_res = json.loads(data)
        # print(type(json_res))
        fname = json_res["results"][0]["name"]["first"]
        # print(fname)
        email = json_res["results"][0]["email"]
        print(email)
    except BaseException as err:
        print(err)

def get_response(url):
    try:
        res = requests.get(url)
        # print(res)
        # print(res.text)
        # print(type(res.text))
        return res.text
    except BaseException as err:
        print(err)

url= "https://randomuser.me/api"
fetch_data(url)