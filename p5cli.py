#!/usr/bin/env python
import sys
import requests

try:
        api_name = sys.argv[1]
        input = sys.argv[2]
except:
        api_name = "null"
        if api_name == 'null':
                sys.exit("usage: p5cli [API Argument] [String] [Value] [HTTP Method]")
try:
        value = sys.argv[3]
        method = sys.argv[4]
except IndexError:
        value = 'null'
        method = 'null'

 
if  api_name != "md5" and api_name != "factorial" and api_name != "fibonacci" and api_name != "i$
        (
                sys.exit("sorry wrong API argument try:\n md5\n factorial\n fibonacci\n is-prime$
        )

url= "http://0.0.0.0:5000/" + api_name + "/" + input 

if api_name == "kv-record":
        data = { 'value': value }
        if method.lower() == 'post': 
                resp = requests.post(url, json=data)
        elif method.lower() == 'put':
                resp = requests.put(url, json=data)
        else:
                sys.exit("usage: p5cli kv-record [String] [Value] [POST or PUT]")

else:
        resp = requests.get(url)

print resp.content
