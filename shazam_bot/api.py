import requests
import pprint
from config import url ,headers

def search_from_api(query):
    querystring = {"term":query,"locale":"en-US","offset":"0","limit":"5"}
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

