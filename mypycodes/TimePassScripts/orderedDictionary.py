import json
import requests
from collections import OrderedDict


with open("new.json", 'r') as jfile:
    json_temp = jfile.read()


loadsdata = json.loads(json_temp)
ordereddictiona = json.loads(json_temp, object_pairs_hook=OrderedDict)
dumpsdata = json.dumps(ordereddictiona)

print loadsdata
print ordereddictiona
print dumpsdata
print json_temp


# parsed_json = json.loads(json_temp)

# print parsed_json