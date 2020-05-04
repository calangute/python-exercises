# keywords to test composite commands in REST
import json
import sys
import os
import requests
import RequestsLibrary

from collections import OrderedDict

from robot.libraries.BuiltIn import BuiltIn

# variables.py file is imported from the VARIABLES_FILE_DIR path provided in the test case
# if VARIABLES_FILE_DIR is not defined , variables.py under main/testcases/ directory is imported
builtin = BuiltIn()
variables_file_path = builtin.get_variable_value("${VARIABLES_FILE_DIR}")
if variables_file_path:
    sys.path.append(os.path.abspath(variables_file_path))
else:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../testcases/')))

import variables


def create_comp_session(session_user, session_password, session_alias='bscs'):
    """creates new HTTP session - not utilized yet in any test cases
    :param session_user: <user name for the session>
    :param session_password:<password for the session>
    :param session_alias:<alias name of the session>
    """
    auth = (session_user, session_password)
    session_create = RequestsLibrary.RequestsLibrary()
    return session_create.create_session(session_alias, variables.RESTURL, auth=auth)


def data_loader(data=None):
    """Consumes a file (if passed) and returns a valid JSON formatted string
    :param data: <input data to be sent along with the request(can be empty)>
    """
    restdata = json.load(open(data), object_pairs_hook=OrderedDict) if data else {}
    return json.dumps(restdata)


def uri_serializer(restcommand, method, data=None, bu_id=""):
    """prepares uri for GET POST PUT in REST
    :param restcommand:
    :param method:
    :param data:
    :param bu_id:
    """
    global uri
    session_change = "?sessionChange={{\"BU_ID\":\"{0}\"}}".format(bu_id) if bu_id else "?"
    parameter = "commandInput={0}".format(data_loader(data)) if data and method.lower() == 'get' else ""
    if method.lower() == 'get':
        delimiter = "&" if session_change and data else ""
        uri = "{0}{1}{2}{3}{4}".format(variables.RESTURL, restcommand, session_change, delimiter, parameter)
    elif method.lower() == 'post' or 'put':
        uri = variables.RESTURL + restcommand + session_change
    return uri.encode("utf-8")


def execute_composite_command(restcommand, method, data=None, bu_id=""):
    """method to perform GET PUT and POST in REST and returns the response text and response status
    :param restcommand: <rest command to be appended to the base REST URL>
    :param method: <any HTTP method accepted by python requests library(case insensitive>
    :param data: <input data to be sent along with the request(can be empty)>
    :param bu_id: <business unit ID for session change(can be empty)>
    usage : Execute Composite Command | <rest command> | <Http Method> | <input data file name with path> | <Business Unit Id> |
    example : Execute Composite Command | '/CIL/6/CUSTOMER.CREATE/' | 'Post' | '../../customerCreate.json' | '2' |
    """
    global resp
    headers = {'content-type': 'application/json'}
    s = requests.Session()
    s.auth = (variables.USER, variables.PASSWORD)
    s.headers.update(headers)
    uri_local = uri_serializer(restcommand, method, data, bu_id)
    if method.lower() in ['get', 'put', 'post']:
        resp = getattr(s, method.lower())(uri_local, data=data_loader(data))
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print "HTTPError occurred:", e.message
        return {'status': resp.status_code, 'content': resp.json()}
        # return resp.status_code,resp.content
    else:
        raise ValueError('HTTP Method name not recognised, please use : get or put or post')


def status_checker(restcommand, method, data=None, bu_id=""):
    """    executes the rest request and returns the status code of the response
    :param restcommand: <rest command to be appended to the base REST URL>
    :param method: <any HTTP method accepted by python requests library(case insensitive>
    :param data:<input data to be sent along with the request(can be empty)>
    :param bu_id:<business unit ID for session change(can be empty)>
    """
    return execute_composite_command(restcommand, method, data, bu_id)["status"]



