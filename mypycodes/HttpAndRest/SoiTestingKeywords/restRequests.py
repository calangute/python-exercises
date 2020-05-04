import requests
import json,ast
import variables
import RequestsLibrary
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn

# restcommand = '/CIL/6/CUSTOMER.READ'
# with open("CustomerCreate.json",'r') as jfile:
#             json_temp= jfile.read()
# parsed = json.dumps(json_temp)
# bu_id = 2
# restdata = json.load(open('j.json'), object_pairs_hook=OrderedDict)
# method ='Get'
def create_new_session(session_user,session_password,session_alias='bscs'):
    auth = (session_user,session_password)
    session_create = RequestsLibrary.RequestsLibrary()
    session_create.create_session(session_alias,variables.RESTURL,auth=auth)

def execute_composite_command(restcommand, method, status,data,bu_id = "", session_alias='bscs'):
    headers = {'content-type':'application/json'}
    session_change = "?sessionChange={{\"BU_ID\":\"{0}\"}}&".format(bu_id) if bu_id else "?"
    restdata = json.load(open(data), object_pairs_hook=OrderedDict) if data else {}
    parameter = "commandInput={0}".format(json.dumps(data)) if restdata and method == 'Get' else ""
    #calling respective methods
    req_call = RequestsLibrary.RequestsLibrary()

    if method == 'Get':
        uri = "{0}{1}{2}".format(restcommand,session_change,parameter)
        print uri
        resp = req_call.get_request(session_alias,uri,headers=headers)
        print resp
    elif method == 'Post':
        uri = restcommand + session_change
        resp = req_call.post_request(session_alias,uri,data=restdata,headers=headers)
        print resp
    builtin = BuiltIn()
    result = builtin.should_be_equal(resp,200)
    return result
# execute_composite_command('https://httpbin.org/get','Get',200)


#create_new_session(variables.USER,variables.PASSWORD)

