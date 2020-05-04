import requests, time
import logging
import json
import ast

#x = '{"search" : {"prmIdPub": "145","sccodePub": "ISD"}, "read" : { "prmId": "145"}}'


with open("jinp.json",'r') as jfile:
            x = jfile.read()


the_dict = json.loads(x)

y = the_dict["search"]

print y

print the_dict["search"], "\n"

print repr(the_dict), "\n"

print ast.literal_eval(json.dumps(x))

print ast.literal_eval(json.dumps(y))