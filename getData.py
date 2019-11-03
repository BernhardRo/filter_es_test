import pymongo
import pandas as pd
import numpy as np
import requests, json, hashlib, urllib, datetime
from dateutil.parser import parse
from secret import  NS_URL, NS_SECRET

NS_AUTHOR = "xDrip-NSEmulator"
TIMEZONE = "Europe/Berlin"


def get_from_nightscout(cnt):
    	#last = requests.get(NS_URL + 'api/v1/treatments?count=1&find[eventType]='+urllib.parse.quote('Exercise'), headers={
            #last = requests.get(NS_URL + 'api/v1/treatments?count=1&find[enteredBy]='+urllib.parse.quote(NS_AUTHOR), headers={
	last = requests.get(NS_URL + 'api/v1/entries?count='+str(cnt)+'&find[type]=sgv&find[device]='+urllib.parse.quote(NS_AUTHOR), headers={
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'api-secret': hashlib.sha1(NS_SECRET.encode()).hexdigest()
	})
	if last.status_code == 200:
		js = last.json()
		return reversed(js)

def main():
    js = get_from_nightscout(100)
    for x in js:
        print(x)
        time = parse(x['sysTime'])
        sgv = x['sgv']


if __name__ == '__main__':
	main()