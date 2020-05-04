import requests
import json,ast
import variables
import re
from collections import OrderedDict

auth = (variables.USER,variables.PASSWORD)
print auth

def execute_composite_command(restcommand, method, status, restdata,bu_id, session_alias):
    headers = {'content-type':'application/json'}
    if restdata:
        data = json.load(open('CustomerCreate.json'), object_pairs_hook=OrderedDict)
        print json.dumps(data)
    elif method == 'Post' or 'Put' and not restdata:
        data = {}
    else
        data = none
delimiter

method = 'booz'
restdata = 'juk'
bu_id = None

if method == 'Post' or 'Put' and not restdata:
        if not bu_id:
            delimiter = '?'
else:
    delimiter = "&"

print delimiter





# parsed_json = json.loads(json_temp)
#
# json.JSONDecoder(object_pairs_hook = collections.OrderedDict).decode(json_temp)
# OrderedDict()
#
# print object_pairs_hook

#
# print parsed_json
#
# d_json = json.dumps(json_temp)
# print d_json

# r = requests.put(variables.RESTURL,auth=auth,json=data)
#
# # r = requests.options(variables.RESTURL)
#
# print r.status_code
#
# print r.content